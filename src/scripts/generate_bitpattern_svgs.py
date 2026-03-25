import wavedrom
import json
import os
import sys

def generate_reg_svg(reg_json, output_path):
    # Ensure config exists
    if 'config' not in reg_json:
        reg_json['config'] = {}

    # Check if bits is already specified
    if 'bits' not in reg_json['config']:
        # Calculate total bits from reg array
        total_bits = 0
        if 'reg' in reg_json:
            for item in reg_json['reg']:
                total_bits += item.get('bits', 1)

        # Default to 8 if <= 8, 16 if <= 16, else leave as is (WaveDrom default)
        if total_bits <= 8:
            reg_json['config']['bits'] = 8
        elif total_bits <= 16:
            reg_json['config']['bits'] = 16

    svg = wavedrom.render(json.dumps(reg_json))
    svg.saveas(output_path)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 generate_bitpattern_svgs.py <json_string> <output_path>")
        sys.exit(1)

    reg_json = json.loads(sys.argv[1])
    output_path = sys.argv[2]

    generate_reg_svg(reg_json, output_path)
