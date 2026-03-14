import yaml
import sys
import os
import requests
from plantuml import PlantUML

def generate_puml(data):
    puml = ["@startuml"]

    # Declarations
    puml.append('robust "CLK" as CLK')
    puml.append('concise "Phase" as SIG')

    signals = data.get('signals', {})
    for sig_name in signals:
        if sig_name == 'CLK': continue
        if sig_name in ['UI_IN', 'UIO', 'UO_OUT']:
            puml.append(f'concise "{sig_name}" as {sig_name}')
        else:
            puml.append(f'binary "{sig_name}" as {sig_name}')

    puml.append("")

    # Time 0 initialization
    puml.append("@0")
    puml.append("CLK is Low")
    puml.append("SIG is {-}")
    for sig_name in signals:
        if sig_name == 'CLK': continue
        puml.append(f"{sig_name} is 0")

    steps = data.get('test_steps', [])
    current_time = 0
    cycle_count = 0
    # Increased max cycles to capture the whole protocol
    max_cycles = 100

    for step in steps:
        if cycle_count >= max_cycles:
            break

        name = step.get('name', 'Step').replace(" ", "_").translate(str.maketrans("", "", "():{}[]&"))
        cycles = step.get('cycles', 1)
        values = step.get('values', {})

        # Apply signal changes at start of step
        puml.append(f"\n@{current_time}")
        puml.append(f'SIG is {name}')
        for sig_name, val in values.items():
            if sig_name == 'CLK': continue
            if isinstance(val, int):
                puml.append(f"{sig_name} is {val}")
            else:
                puml.append(f"{sig_name} is \"{val}\"")

        for _ in range(cycles):
            if cycle_count >= max_cycles:
                break
            # Clock pulse
            puml.append(f"@{current_time}")
            puml.append("CLK is High")
            puml.append(f"@{current_time + 0.5}")
            puml.append("CLK is Low")
            current_time += 1
            cycle_count += 1

    puml.append("@enduml")
    return "\n".join(puml)

def render_png(puml_content, output_path):
    server = PlantUML(url='http://www.plantuml.com/plantuml/img/')
    try:
        url = server.get_url(puml_content)
        print(f"Fetching from: {url}")
        response = requests.get(url)
        if response.content.startswith(b'\x89PNG'):
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"Successfully rendered to {output_path}")
        else:
            print(f"Failed to render: HTTP {response.status_code}")
    except Exception as e:
        print(f"Error rendering: {e}")

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
    print(f"Generated PlantUML source: {puml_path}")

    render_png(puml_content, png_path)
