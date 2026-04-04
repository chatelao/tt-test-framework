import os
import yaml
import subprocess
import shutil
import glob
import sys

DATA_DIR = "src/data"
WASM_DIR = "wasm"
WRAPPER_CPP = "src/scripts/wasm_top.cpp"
VERILATOR_INCLUDE = "/usr/share/verilator/include"

def compile_project(yaml_path):
    filename = os.path.basename(yaml_path)
    if not filename.startswith('tt'):
        return

    project_id = filename.split('_')[0]

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
        if 'verilog' not in language and 'systemverilog' not in language:
            print(f"Skipping {project_id}: Language is '{language}', not Verilog/SystemVerilog")
            return

        top_module = project_info.get('top_module')
        source_files = project_info.get('source_files', [])

        if not top_module or not source_files:
            print(f"Skipping {project_id}: top_module or source_files missing in info.yaml")
            return

        # Prepare verilator command
        v_sources = [os.path.join(temp_dir, "src", f) for f in source_files]
        # Check if all source files exist
        missing_files = [f for f in v_sources if not os.path.exists(f)]
        if missing_files:
             print(f"Warning for {project_id}: Some source files missing: {missing_files}")
             v_sources = [f for f in v_sources if os.path.exists(f)]

        if not v_sources:
             print(f"Skipping {project_id}: No valid source files found in src/")
             return

        print(f"Verilating {project_id}...")
        verilator_cmd = [
            "verilator", "--cc", "--prefix", "Vtop",
            "-I" + os.path.join(temp_dir, "src"),
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
        # We need to compile Verilator support files and generated files
        verilated_files = [
            os.path.join(VERILATOR_INCLUDE, "verilated.cpp"),
            os.path.join(VERILATOR_INCLUDE, "verilated_threads.cpp")
        ]

        cpp_files = glob.glob(os.path.join(obj_dir, "*.cpp"))
        # Some files might not exist if we use glob.glob on a pattern that verilator doesn't always produce.
        # But here we are using glob.glob(os.path.join(obj_dir, "*.cpp")) which should only return existing files.
        # The error "No such file or directory" for a file returned by glob usually means a race condition
        # or that glob returned something that emcc can't find (unlikely).
        # Wait a bit to ensure filesystem sync? No, let's just be sure they exist.
        cpp_files = [f for f in cpp_files if os.path.exists(f)]

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
