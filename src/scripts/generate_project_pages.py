import os
import yaml
import re
import subprocess
import json

def generate_markdown(pid, yaml_data, svg_path):
    project_name = yaml_data.get('project', f'Project {pid}')
    source_url = yaml_data.get('metadata', {}).get('source', '')

    signals = yaml_data.get('signals', {})

    md_content = f"# {project_name}\n\n"

    if source_url:
        md_content += f"**Source:** [{source_url}]({source_url})\n\n"

    md_content += f"**TinyTapeout Project Page:** [https://app.tinytapeout.com/projects/{pid}](https://app.tinytapeout.com/projects/{pid})\n\n"

    md_content += "## Input/Output Definitions\n\n"
    md_content += "| Signal | Type | Width |\n"
    md_content += "|--------|------|-------|\n"

    for sig_name, sig_info in signals.items():
        stype = sig_info.get('type', 'N/A')
        width = sig_info.get('width', 'N/A')
        md_content += f"| {sig_name} | {stype} | {width} |\n"

    if 'bitfields' in yaml_data:
        md_content += "\n## Bit Patterns\n\n"
        for group in yaml_data['bitfields']:
            md_content += f"### {group['name']}\n"
            for item in group['items']:
                md_content += f"- **{item['signal']}**: {item['description']}\n"
                svg_name = item['svg']
                if not svg_name.endswith('.svg'):
                    svg_name += '.svg'

                # Check if SVG exists, if not generate it
                svg_filepath = os.path.join('waveforms', svg_name)
                if not os.path.exists(svg_filepath):
                    reg_json = item['reg']
                    cmd = ['python3', 'src/scripts/generate_bitpattern_svgs.py', json.dumps(reg_json), svg_filepath]
                    try:
                        subprocess.run(cmd, check=True)
                        print(f"Generated {svg_filepath} for {pid}")
                    except subprocess.CalledProcessError as e:
                        print(f"Error generating SVG {svg_filepath}: {e}")

                md_content += f"![{item['signal']} {group['name']}](../../waveforms/{svg_name})\n"
            md_content += "\n"

    md_content += "\n## Test Waveform\n\n"
    if svg_path and os.path.exists(svg_path):
        md_content += f"![Waveform](../../{svg_path})\n"
    else:
        md_content += "Waveform not available.\n"

    return md_content

def main():
    data_dir = 'src/data'
    projects_dir = 'src/docs'
    waveforms_dir = 'waveforms'

    if not os.path.exists(projects_dir):
        os.makedirs(projects_dir)

    # Collect bitfield SVG names to exclude them from being chosen as main waveform
    bitfield_svgs = set()
    for filename in os.listdir(data_dir):
        if filename.endswith('.yaml'):
            with open(os.path.join(data_dir, filename), 'r') as f:
                try:
                    ydata = yaml.safe_load(f)
                    if ydata and 'bitfields' in ydata:
                        for group in ydata['bitfields']:
                            for item in group['items']:
                                b_svg = item['svg']
                                if not b_svg.endswith('.svg'):
                                    b_svg += '.svg'
                                bitfield_svgs.add(b_svg)
                except:
                    pass

    for filename in os.listdir(data_dir):
        if filename.endswith('.yaml') and filename.startswith('tt'):
            match = re.search(r'tt(\d+)', filename)
            if not match:
                continue
            pid = match.group(1)

            yaml_path = os.path.join(data_dir, filename)
            with open(yaml_path, 'r') as f:
                try:
                    yaml_data = yaml.safe_load(f)
                except yaml.YAMLError:
                    print(f"Error reading {yaml_path}")
                    continue

            if not yaml_data:
                continue

            # Find the main waveform SVG
            svg_path = ""
            potential_svgs = []
            for f in os.listdir(waveforms_dir):
                if f.startswith(f"tt{pid}") and f.endswith(".svg"):
                    if f not in bitfield_svgs:
                        potential_svgs.append(f)

            if potential_svgs:
                # Prefer shortest name that is not a bitfield
                potential_svgs.sort(key=len)
                svg_path = os.path.join(waveforms_dir, potential_svgs[0])
            else:
                # Fallback to any SVG for this PID if no non-bitfield one exists
                for f in os.listdir(waveforms_dir):
                    if f.startswith(f"tt{pid}") and f.endswith(".svg"):
                        svg_path = os.path.join(waveforms_dir, f)
                        break

            md_content = generate_markdown(pid, yaml_data, svg_path)

            with open(os.path.join(projects_dir, f"tt{pid}.md"), 'w') as f:
                f.write(md_content)
            print(f"Generated src/docs/tt{pid}.md")

if __name__ == "__main__":
    main()
