import os
import yaml
import subprocess
import pytest
import sys

def test_generator(tmp_path):
    test_yaml = tmp_path / "test_case.yaml"

    data = {
        "project": "test",
        "signals": {"SIG": {"type": "input", "width": 1}},
        "test_steps": [{"name": "Step 1", "cycles": 1, "values": {"SIG": 1}}]
    }

    with open(test_yaml, "w") as f:
        yaml.dump(data, f)

    # Use sys.executable to match the environment
    result = subprocess.run([sys.executable, "src/scripts/generate_waveform.py", str(test_yaml)], capture_output=True, text=True)
    assert result.returncode == 0
    assert os.path.exists("images/test_case.svg")

    with open("images/test_case.svg", "r") as f:
        content = f.read()
        assert "<svg" in content
        assert "SIG" in content

def test_generator_multiple_cases(tmp_path):
    test_yaml = tmp_path / "multi_case.yaml"

    data = {
        "project": "multi_test",
        "signals": {"SIG": {"type": "input", "width": 1}},
        "test_cases": [
            {
                "name": "CaseA",
                "test_steps": [{"name": "Step A", "cycles": 1, "values": {"SIG": 1}}]
            },
            {
                "name": "CaseB",
                "test_steps": [{"name": "Step B", "cycles": 1, "values": {"SIG": 0}}]
            }
        ]
    }

    with open(test_yaml, "w") as f:
        yaml.dump(data, f)

    result = subprocess.run([sys.executable, "src/scripts/generate_waveform.py", str(test_yaml)], capture_output=True, text=True)
    assert result.returncode == 0

    assert os.path.exists("images/multi_case_CaseA.svg")
    assert os.path.exists("images/multi_case_CaseB.svg")

    with open("images/multi_case_CaseA.svg", "r") as f:
        content = f.read()
        assert "SIG" in content

    with open("images/multi_case_CaseB.svg", "r") as f:
        content = f.read()
        assert "SIG" in content
