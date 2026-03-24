import wavedrom
import json
import os
import sys

def generate_reg_svg(reg_json, output_path):
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
