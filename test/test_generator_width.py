import os
import yaml
import subprocess
import sys

def test_generator_concise_width(tmp_path):
    test_yaml = tmp_path / "concise_width.yaml"

    data = {
        "project": "test_concise",
        "signals": {
            "BUS": {"type": "input", "width": 4},
            "BIT": {"type": "input", "width": 1}
        },
        "test_steps": [{"name": "Step 1", "cycles": 1, "values": {"BUS": 0xA, "BIT": 1}}]
    }

    with open(test_yaml, "w") as f:
        yaml.dump(data, f)

    result = subprocess.run([sys.executable, "src/scripts/generate_waveform.py", str(test_yaml)], capture_output=True, text=True)
    assert result.returncode == 0

    svg_file = "waveforms/concise_width.svg"
    assert os.path.exists(svg_file)

    with open(svg_file, "r") as f:
        content = f.read()
        assert "BUS" in content
        assert "BIT" in content
        assert "10" in content
