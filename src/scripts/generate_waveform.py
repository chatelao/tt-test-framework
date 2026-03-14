import yaml
import sys
import os
import json
import argparse
import wavedrom

def generate_wavedrom_json(data, test_steps):
    signals_config = data.get('signals', {})

    # Calculate total cycles
    total_cycles = sum(step.get('cycles', 1) for step in test_steps)
    total_cycles = min(total_cycles, 100)

    # Initialize timelines
    timelines = {}
    for sig_name in signals_config:
        timelines[sig_name] = [None] * total_cycles

    phase_timeline = [None] * total_cycles

    current_cycle = 0
    for step in test_steps:
        if current_cycle >= total_cycles: break

        cycles = step.get('cycles', 1)
        values = step.get('values', {})
        name = step.get('name', 'Step')

        for i in range(cycles):
            if current_cycle >= total_cycles: break

            if i == 0:
                phase_timeline[current_cycle] = name
            else:
                phase_timeline[current_cycle] = "."

            for sig_name in signals_config:
                if sig_name == 'CLK': continue
                val = values.get(sig_name)
                if val is not None:
                    timelines[sig_name][current_cycle] = val
                else:
                    timelines[sig_name][current_cycle] = None

            current_cycle += 1

    # Default initialization for cycle 0 if None
    for sig_name in timelines:
        if sig_name == 'CLK': continue
        if timelines[sig_name][0] is None:
            timelines[sig_name][0] = 0

    wd_signals = []

    # Phase signal first
    phase_wave = ""
    phase_data = []
    for val in phase_timeline:
        if val is None or val == ".":
            phase_wave += "."
        else:
            phase_wave += "2"
            phase_data.append(val)
    wd_signals.append({"name": "Phase", "wave": phase_wave, "data": phase_data})

    # CLK signal
    wd_signals.append({"name": "CLK", "wave": "p" + "." * (total_cycles - 1)})

    for sig_name, sig_info in signals_config.items():
        if sig_name == 'CLK': continue

        width = sig_info.get('width', 1)
        is_concise = width > 1 or sig_name in ['UI_IN', 'UIO', 'UO_OUT']

        wave = ""
        data_list = []
        last_val = None

        for val in timelines[sig_name]:
            if val is None:
                wave += "."
            else:
                if is_concise:
                    if val == last_val:
                        wave += "."
                    else:
                        wave += "="
                        data_list.append(str(val))
                else:
                    # Binary
                    if isinstance(val, int):
                        if val != 0:
                            wave += "1"
                        else:
                            wave += "0"
                    elif str(val).lower() in ['high', '1']:
                        wave += "1"
                    else:
                        wave += "0"
                last_val = val

        sig_entry = {"name": sig_name, "wave": wave}
        if data_list:
            sig_entry["data"] = data_list
        wd_signals.append(sig_entry)

    return {"signal": wd_signals}

def process_test_case(data, test_steps, output_base, case_name=None, outdir=None, suffix=None):
    wd_json = generate_wavedrom_json(data, test_steps)
    json_str = json.dumps(wd_json)

    name_suffix = f"_{case_name}" if case_name else ""
    if suffix:
        name_suffix += suffix

    if outdir:
        svg_path = os.path.join(outdir, f"{output_base}{name_suffix}.svg")
    else:
        svg_path = os.path.join("images", f"{output_base}{name_suffix}.svg")

    if outdir:
        os.makedirs(outdir, exist_ok=True)
    else:
        os.makedirs("images", exist_ok=True)

    # Render SVG
    svg = wavedrom.render(json_str)
    svg.saveas(svg_path)
    print(f"Successfully rendered to {svg_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate WaveDrom timing diagrams from YAML test definitions.')
    parser.add_argument('input_yaml', help='Path to the input YAML file')
    parser.add_argument('--outdir', help='Optional output directory for SVG images (defaults to images/)')
    parser.add_argument('--suffix', help='Optional suffix for the output filename')

    args = parser.parse_args()

    with open(args.input_yaml, 'r') as f:
        data = yaml.safe_load(f)

    base_name = os.path.splitext(os.path.basename(args.input_yaml))[0]

    if 'test_cases' in data:
        for case in data['test_cases']:
            process_test_case(data, case['test_steps'], base_name, case['name'], outdir=args.outdir, suffix=args.suffix)
    elif 'test_steps' in data:
        process_test_case(data, data['test_steps'], base_name, outdir=args.outdir, suffix=args.suffix)
    else:
        print("Error: No test_steps or test_cases found in YAML.")
        sys.exit(1)
