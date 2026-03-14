import yaml
import sys
import os
import requests
import zlib

def plantuml_encode(text):
    # Mapping for base64 variant used by PlantUML
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"

    def encode_6bit(b):
        return alphabet[b & 0x3F]

    def encode_3bytes(b1, b2, b3):
        c1 = b1 >> 2
        c2 = ((b1 & 0x3) << 4) | (b2 >> 4)
        c3 = ((b2 & 0xF) << 2) | (b3 >> 6)
        c4 = b3 & 0x3F
        res = ""
        for c in [c1, c2, c3, c4]:
            res += encode_6bit(c & 0x3F)
        return res

    # PlantUML expects standard deflate
    compressor = zlib.compressobj(level=9, method=zlib.DEFLATED, wbits=-15)
    compressed_string = compressor.compress(text.encode('utf-8'))
    compressed_string += compressor.flush()

    res = ""
    for i in range(0, len(compressed_string), 3):
        if i + 2 < len(compressed_string):
            res += encode_3bytes(compressed_string[i], compressed_string[i+1], compressed_string[i+2])
        elif i + 1 < len(compressed_string):
            res += encode_3bytes(compressed_string[i], compressed_string[i+1], 0)
        else:
            res += encode_3bytes(compressed_string[i], 0, 0)
    return res

def generate_puml(data):
    puml = ["@startuml", "robust \"CLK\" as CLK", "concise \"Signals\" as SIG"]

    signals = data.get('signals', {})
    for sig_name, sig_info in signals.items():
        if sig_name != 'CLK':
            puml.append(f'robust "{sig_name}" as {sig_name}')

    current_time = 0
    puml.append("")

    for sig_name in signals:
        if sig_name == 'CLK':
            puml.append(f"CLK is Low")
        else:
            puml.append(f"{sig_name} is {{undef}}")

    # Take only first few steps to keep it small for rendering
    steps = data.get('test_steps', [])
    if len(steps) > 8:
        steps = steps[:8]

    for step in steps:
        name = step.get('name', 'Step')
        cycles = step.get('cycles', 1)
        if cycles > 2:
            cycles = 2
            name += " (trunc)"
        values = step.get('values', {})

        puml.append(f"\n@ {current_time}")
        puml.append(f'SIG is "{name}"')

        for sig_name, val in values.items():
            if isinstance(val, int):
                width = signals.get(sig_name, {}).get('width', 1)
                if width == 1:
                    puml.append(f"{sig_name} is {'High' if val else 'Low'}")
                else:
                    puml.append(f'{sig_name} is "{hex(val)}"')
            else:
                puml.append(f'{sig_name} is "{val}"')

        for i in range(cycles):
            puml.append(f"@ {current_time}")
            puml.append("CLK is High")
            puml.append(f"@ {current_time + 0.5}")
            puml.append("CLK is Low")
            current_time += 1

    puml.append(f"@ {current_time}")
    puml.append("@enduml")
    return "\n".join(puml)

def render_png(puml_content, output_path):
    # Try the hex encoding method with ~h
    hex_encoded = puml_content.encode('utf-8').hex()
    url = f"https://www.plantuml.com/plantuml/png/~h{hex_encoded}"

    print(f"Requesting: {url}")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"Successfully rendered to {output_path}")
        else:
            print(f"Failed to render (status {response.status_code})")
    except Exception as e:
        print(f"Error calling PlantUML API: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_waveform.py <input_yaml>")
        sys.exit(1)

    input_yaml = sys.argv[1]
    with open(input_yaml, 'r') as f:
        data = yaml.safe_load(f)

    puml_content = generate_puml(data)

    base_name = os.path.splitext(os.path.basename(input_yaml))[0]
    puml_path = os.path.join("src/images", f"{base_name}.puml")
    png_path = os.path.join("src/images", f"{base_name}.png")

    os.makedirs("src/images", exist_ok=True)
    with open(puml_path, 'w') as f:
        f.write(puml_content)
    print(f"Generated PlantUML: {puml_path}")

    render_png(puml_content, png_path)
