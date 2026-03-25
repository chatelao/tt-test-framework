import os
import requests
import re
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True

def get_info_yaml_content(source_url):
    if not source_url:
        return None

    # Try common branch names
    branches = ['main', 'master']

    # Convert github url to raw content url
    # github.com/user/repo -> raw.githubusercontent.com/user/repo/branch/info.yaml
    match = re.search(r"github\.com/([^/]+)/([^/]+)", source_url)
    if not match:
        return None

    user, repo = match.groups()
    repo = repo.split('/')[0] # remove any suffix

    for branch in branches:
        # Check standard and src/ directory for info.yaml
        urls = [
            f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/info.yaml",
            f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/src/info.yaml"
        ]
        for url in urls:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    return response.text
            except:
                pass
    return None

def parse_pinout(info_yaml_content):
    if not info_yaml_content:
        return {}

    try:
        data = yaml.load(info_yaml_content)
        if not data or 'pinout' not in data:
            return {}
        return data['pinout']
    except:
        return {}

def group_pins(pinout, prefix):
    # prefix is 'ui', 'uo', or 'uio'
    pins = []
    for i in range(8):
        key = f"{prefix}[{i}]"
        label = pinout.get(key, "").strip()
        # Clean up label (sometimes it has (n))
        label = re.sub(r"\s*\(\d+\)\s*", "", label).strip()
        pins.append(label)

    groups = []
    if all(not p for p in pins):
        return [{"name": "Data", "bits": 8}]

    i = 0
    while i < 8:
        label = pins[i]
        j = i + 1
        while j < 8 and pins[j] == label:
            j += 1

        # If label is empty, mark as unused/reserved
        if not label:
            groups.append({"bits": j - i, "name": "unused"})
        else:
            groups.append({"name": label, "bits": j - i})
        i = j
    return groups

def generate_bitfields(pid, source_url, signals):
    info_yaml = get_info_yaml_content(source_url)
    pinout = parse_pinout(info_yaml)

    bitfields = []

    # Process ui_in
    if 'ui_in' in signals:
        ui_groups = group_pins(pinout, 'ui')
        bitfields.append({
            "name": "Input (ui_in)",
            "items": [{
                "signal": "ui_in",
                "description": "Input signal mappings",
                "svg": f"tt{pid}_ui_in",
                "reg": {"reg": ui_groups, "config": {"hspace": 800, "bits": 8}}
            }]
        })

    # Process uo_out
    if 'uo_out' in signals:
        uo_groups = group_pins(pinout, 'uo')
        bitfields.append({
            "name": "Output (uo_out)",
            "items": [{
                "signal": "uo_out",
                "description": "Output signal mappings",
                "svg": f"tt{pid}_uo_out",
                "reg": {"reg": uo_groups, "config": {"hspace": 800, "bits": 8}}
            }]
        })

    # Process uio_in
    if 'uio_in' in signals:
        uio_groups = group_pins(pinout, 'uio')
        bitfields.append({
            "name": "Bidirectional (uio_in)",
            "items": [{
                "signal": "uio_in",
                "description": "Bidirectional signal mappings",
                "svg": f"tt{pid}_uio_in",
                "reg": {"reg": uio_groups, "config": {"hspace": 800, "bits": 8}}
            }]
        })

    return bitfields

def main():
    data_dir = 'src/data'
    for filename in os.listdir(data_dir):
        if filename.endswith('.yaml') and filename.startswith('tt'):
            filepath = os.path.join(data_dir, filename)
            match = re.search(r'tt(\d+)', filename)
            pid = match.group(1)

            with open(filepath, 'r') as f:
                try:
                    data = yaml.load(f)
                except:
                    continue

            if not data: continue

            # Skip if manually updated projects
            if pid in ['3990', '3415', '3641', '3991']:
                print(f"Skipping manually maintained {pid}")
                continue

            source_url = data.get('metadata', {}).get('source', '')
            signals = data.get('signals', {})

            print(f"Processing {pid}...")
            bitfields = generate_bitfields(pid, source_url, signals)
            if bitfields:
                data['bitfields'] = bitfields
                with open(filepath, 'w') as f:
                    yaml.dump(data, f)
                print(f"Updated {pid} with bitfields.")

if __name__ == "__main__":
    main()
