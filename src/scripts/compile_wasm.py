import os
import yaml
import subprocess
import shutil
import glob
import sys

DATA_DIR = "src/data"
WASM_DIR = "wasm"
WRAPPER_CPP = "src/scripts/wasm_top.cpp"

def get_verilator_include():
    try:
        result = subprocess.run(["verilator", "-V"], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if "VERILATOR_ROOT" in line and "=" in line:
                root = line.split("=")[1].strip()
                if root:
                    return os.path.join(root, "include")
    except Exception:
        pass
    return "/usr/share/verilator/include"

VERILATOR_INCLUDE = get_verilator_include()

def compile_project(yaml_path):
    filename = os.path.basename(yaml_path)
    if not filename.startswith('tt'):
        return

    project_id = filename.split('_')[0].split('.')[0]

    if os.path.exists(os.path.join(WASM_DIR, f"{project_id}.js")):
        print(f"Skipping {project_id}: already compiled")
        return

    with open(yaml_path, 'r') as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError:
            print(f"Skipping {filename}: Invalid YAML")
            return

    source_url = data.get('metadata', {}).get('source')
    if not source_url:
        print(f"Skipping {project_id}: No source URL in metadata")
        return

    temp_dir = f"temp_{project_id}"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

    try:
        print(f"--- Processing {project_id} ---")
        print(f"Cloning {source_url}...")
        result = subprocess.run(["git", "clone", "--depth", "1", source_url, temp_dir], capture_output=True)
        if result.returncode != 0:
            print(f"Failed to clone {source_url}: {result.stderr.decode()}")
            return

        info_yaml_path = os.path.join(temp_dir, "info.yaml")
        if not os.path.exists(info_yaml_path):
            print(f"Skipping {project_id}: No info.yaml found in repo")
            return

        with open(info_yaml_path, 'r') as f:
            try:
                info = yaml.safe_load(f)
            except yaml.YAMLError:
                print(f"Skipping {project_id}: Invalid info.yaml")
                return

        project_info = info.get('project', {})
        language = project_info.get('language', '').lower()

        top_module = project_info.get('top_module')
        source_files = project_info.get('source_files', [])

        # Robust check for Verilog/SystemVerilog
        is_verilog = 'verilog' in language or 'systemverilog' in language
        if not is_verilog:
            # Check if there are .v or .sv files in src/ anyway
            if glob.glob(os.path.join(temp_dir, "src", "**", "*.v"), recursive=True) or \
               glob.glob(os.path.join(temp_dir, "src", "**", "*.sv"), recursive=True):
                is_verilog = True

        if not is_verilog:
            print(f"Skipping {project_id}: Language is '{language}', not Verilog/SystemVerilog")
            return

        if not top_module:
            print(f"Skipping {project_id}: top_module missing in info.yaml")
            return

        # Prepare verilator command
        src_dir = os.path.join(temp_dir, "src")
        include_dirs = [src_dir]
        for root, dirs, files in os.walk(src_dir):
            for d in dirs:
                include_dirs.append(os.path.join(root, d))

        v_sources = []
        if source_files:
            for f in source_files:
                found = False
                for d in include_dirs:
                    full_path = os.path.join(d, f)
                    if os.path.exists(full_path):
                        v_sources.append(full_path)
                        found = True
                        break
                if not found:
                    print(f"Warning for {project_id}: Source file {f} not found")
        else:
            # Try to find all .v and .sv files if source_files is empty
            v_sources = glob.glob(os.path.join(temp_dir, "src", "**", "*.v"), recursive=True) + \
                        glob.glob(os.path.join(temp_dir, "src", "**", "*.sv"), recursive=True)

        if not v_sources:
             print(f"Skipping {project_id}: No valid source files found in src/")
             return

        print(f"Verilating {project_id}...")
        verilator_cmd = [
            "verilator", "--cc", "--prefix", "Vtop",
        ] + ["-I" + d for d in include_dirs] + [
            "--top-module", top_module,
            "-Wno-fatal", # Don't stop on warnings
        ] + v_sources

        v_result = subprocess.run(verilator_cmd, capture_output=True)
        if v_result.returncode != 0:
            print(f"Verilator failed for {project_id}: {v_result.stderr.decode()}")
            return

        # Compile with emcc
        print(f"Compiling {project_id} to WASM...")
        obj_dir = "obj_dir"
        verilated_files = [
            os.path.join(VERILATOR_INCLUDE, "verilated.cpp"),
            os.path.join(VERILATOR_INCLUDE, "verilated_threads.cpp")
        ]

        vtop_cpp_files = [f for f in glob.glob(os.path.join(obj_dir, "Vtop*.cpp")) if os.path.exists(f)]

        emcc_cmd = [
            "emcc", "-O3", "--bind",
            "-DVL_IGNORE_UNKNOWN_ARCH",
            "-I" + obj_dir,
            "-I" + VERILATOR_INCLUDE,
            "-I" + os.path.join(VERILATOR_INCLUDE, "vltstd"),
            WRAPPER_CPP
        ] + verilated_files + vtop_cpp_files + [
            "-o", os.path.join(WASM_DIR, f"{project_id}.js"),
            "-s", "MODULARIZE=1",
            "-s", "EXPORT_NAME='" + project_id + "'",
            "-s", "ENVIRONMENT='web,node'",
            "-s", "ALLOW_MEMORY_GROWTH=1"
        ]

        e_result = subprocess.run(emcc_cmd, capture_output=True)
        if e_result.returncode != 0:
            print(f"Emcc failed for {project_id}: {e_result.stderr.decode()}")
            return

        print(f"Successfully compiled {project_id}")

    except Exception as e:
        print(f"An unexpected error occurred for {project_id}: {e}")
    finally:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        if os.path.exists("obj_dir"):
            shutil.rmtree("obj_dir")

def main():
    if not os.path.exists(WASM_DIR):
        os.makedirs(WASM_DIR)

    yaml_files = sorted(glob.glob(os.path.join(DATA_DIR, "*.yaml")))

    if len(sys.argv) > 1:
        target_ids = sys.argv[1:]
        filtered_files = []
        for target_id in target_ids:
            for f in yaml_files:
                if target_id in os.path.basename(f):
                    filtered_files.append(f)
        yaml_files = filtered_files

    for yaml_file in yaml_files:
        compile_project(yaml_file)

if __name__ == "__main__":
    main()
