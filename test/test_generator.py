import os
import yaml
import subprocess
import pytest
import sys

def test_generator_single(tmp_path):
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
    assert os.path.exists("src/images/test_case.puml")

    with open("src/images/test_case.puml", "r") as f:
        content = f.read()
        assert "@startuml" in content
        assert "SIG is 1" in content
        assert "SIG is Step_1" in content

def test_generator_multiple(tmp_path):
    test_yaml = tmp_path / "multi_test.yaml"

    data = {
        "project": "test",
        "signals": {"SIG": {"type": "input", "width": 1}},
        "test_cases": [
            {"name": "Case A", "test_steps": [{"name": "Step A", "cycles": 1, "values": {"SIG": 1}}]},
            {"name": "Case B", "test_steps": [{"name": "Step B", "cycles": 1, "values": {"SIG": 0}}]}
        ]
    }

    with open(test_yaml, "w") as f:
        yaml.dump(data, f)

    result = subprocess.run([sys.executable, "src/scripts/generate_waveform.py", str(test_yaml)], capture_output=True, text=True)
    assert result.returncode == 0
    assert os.path.exists("src/images/multi_test_Case_A.puml")
    assert os.path.exists("src/images/multi_test_Case_B.puml")

    with open("src/images/multi_test_Case_A.puml", "r") as f:
        content = f.read()
        assert "SIG is 1" in content
        assert "SIG is Step_A" in content

    with open("src/images/multi_test_Case_B.puml", "r") as f:
        content = f.read()
        assert "SIG is 0" in content
        assert "SIG is Step_B" in content
