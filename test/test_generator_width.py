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

    puml_file = "src/puml/concise_width.puml"
    assert os.path.exists(puml_file)

    with open(puml_file, "r") as f:
        content = f.read()
        assert 'concise "BUS" as BUS' in content
        assert 'binary "BIT" as BIT' in content
        assert "BUS is 10" in content
        assert "BIT is 1" in content
