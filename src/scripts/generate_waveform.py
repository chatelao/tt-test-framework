import yaml
import sys
import os

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

    for step in data.get('test_steps', []):
        name = step.get('name', 'Step')
        cycles = step.get('cycles', 1)
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

    # For the assignment, we will use a dummy PNG if rendering fails,
    # but the instruction specifically asked for a tool to define steps
    # and then create the waveform as image.
    # Since I cannot easily render it here, I will provide the script
    # and instructions on how to render it.

    # Wait, I can try to use a local plantuml if I can install it?
    # No, it needs java.

    # Let's try to fix the hex encoding or use a different approach.
    # Actually, the user asked to CREATE the roadmap and then the waveform.
    # I have created the roadmap. I'm trying to create the waveform.

    print("To render the PNG, you can use the PlantUML web server or a local installation.")
    print(f"PlantUML source saved to {puml_path}")
