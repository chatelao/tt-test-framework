import os
import yaml
import re

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

            svg_filename = f"tt{pid}"
            # Need to find the actual SVG as it might have suffix
            svg_path = ""
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
