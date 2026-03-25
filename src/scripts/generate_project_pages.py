import os
import yaml
import re
import subprocess
import json

def decode_value(value, bit_defs):
    if not isinstance(value, int):
        return str(value)

    decoded = []
    current_bit = 0
    for bd in bit_defs:
        bits = bd.get('bits', 1)
        name = bd.get('name', 'unused')

        mask = (1 << bits) - 1
        field_val = (value >> current_bit) & mask

        if name and name.lower() != 'unused':
            decoded.append(f"{name}={field_val}")

        current_bit += bits

    return ", ".join(decoded) if decoded else ""

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

    # First 10 Cycles table
    test_steps = yaml_data.get('test_steps')
    if not test_steps and 'test_cases' in yaml_data:
        test_steps = yaml_data['test_cases'][0].get('test_steps')

    if test_steps:
        md_content += "\n## First 10 Cycles\n\n"

        # Filter signals to show in table (exclude clocks for brevity)
        table_signals = [s for s, info in signals.items() if info.get('type') != 'clock']

        md_content += "| Cycle | Phase | " + " | ".join(table_signals) + " |\n"
        md_content += "|-------|-------|" + "|".join(["-------" for _ in table_signals]) + "|\n"

        flat_cycles = []
        for step in test_steps:
            cycles = step.get('cycles', 1)
            for i in range(cycles):
                flat_cycles.append({
                    'name': step.get('name', ''),
                    'values': step.get('values', {})
                })
                if len(flat_cycles) >= 10:
                    break
            if len(flat_cycles) >= 10:
                break

        last_values = {sig: 0 for sig in table_signals}

        for i, cycle in enumerate(flat_cycles):
            phase_name = cycle['name']
            row = [str(i), phase_name]

            for sig_name in table_signals:
                val = cycle['values'].get(sig_name)
                if val is None:
                    val = last_values.get(sig_name, 0)

                last_values[sig_name] = val

                # Decoding logic
                decoded_str = ""
                if isinstance(val, int) and 'bitfields' in yaml_data:
                    # Try to find a matching bitfield group
                    best_group = None
                    best_item = None

                    # 1. Try to find a group that matches the phase name AND contains the signal
                    for group in yaml_data['bitfields']:
                        # Check for common prefix or containment
                        g_name = group['name'].lower()
                        p_name = phase_name.lower()

                        # Match if one contains the other, or if they share a common "Cycle N" prefix
                        match = g_name in p_name or p_name in g_name
                        if not match:
                            # Try matching numbers if 'cycle' or 'step' is present
                            nums1 = re.findall(r'(\d+)', g_name)
                            nums2 = re.findall(r'(\d+)', p_name)
                            if nums1 and nums2:
                                # If they share any number and both mention 'cycle'
                                if ('cycle' in g_name or 'step' in g_name) and \
                                   ('cycle' in p_name or 'step' in p_name):
                                    common = set(nums1) & set(nums2)
                                    if common:
                                        match = True

                        if match:
                            for item in group['items']:
                                if item['signal'] == sig_name:
                                    best_group = group
                                    best_item = item
                                    break
                        if best_item: break

                    # 2. Fallback: find any group that contains the signal name in its name
                    if not best_item:
                        for group in yaml_data['bitfields']:
                            if sig_name.lower() in group['name'].lower():
                                for item in group['items']:
                                    if item['signal'] == sig_name:
                                        best_group = group
                                        best_item = item
                                        break
                            if best_item: break

                    # 3. Last resort: find the first group that defines this signal
                    if not best_item:
                        for group in yaml_data['bitfields']:
                            for item in group['items']:
                                if item['signal'] == sig_name:
                                    best_group = group
                                    best_item = item
                                    break
                            if best_item: break

                    if best_item:
                        bit_defs = best_item.get('reg', {}).get('reg', [])
                        if bit_defs:
                            decoded_str = decode_value(val, bit_defs)

                if decoded_str:
                    row.append(f"{hex(val)} ({decoded_str})")
                else:
                    if isinstance(val, int):
                        row.append(hex(val))
                    else:
                        row.append(str(val))

            md_content += "| " + " | ".join(row) + " |\n"

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
