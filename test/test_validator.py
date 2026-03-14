import os
import yaml
import subprocess
import pytest
import sys

def test_validator_valid_single(tmp_path):
    test_yaml = tmp_path / "valid_single.yaml"
    data = {
        "project": "test_project",
        "signals": {
            "CLK": {"type": "clock", "width": 1},
            "DATA": {"type": "input", "width": 8}
        },
        "test_steps": [
            {"name": "Step 1", "cycles": 1, "values": {"DATA": 0xAA}}
        ]
    }
    with open(test_yaml, "w") as f:
        yaml.dump(data, f)

    result = subprocess.run([sys.executable, "src/scripts/validate_yaml.py", str(test_yaml)], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Validation successful" in result.stdout

def test_validator_valid_multiple(tmp_path):
    test_yaml = tmp_path / "valid_multiple.yaml"
    data = {
        "project": "test_project",
        "signals": {
            "CLK": {"type": "clock", "width": 1},
            "DATA": {"type": "input", "width": 8}
        },
        "test_cases": [
            {
                "name": "Case 1",
                "test_steps": [{"name": "Step 1", "cycles": 1, "values": {"DATA": 0xAA}}]
            },
            {
                "name": "Case 2",
                "test_steps": [{"name": "Step 2", "cycles": 1, "values": {"DATA": 0xBB}}]
            }
        ]
    }
    with open(test_yaml, "w") as f:
        yaml.dump(data, f)

    result = subprocess.run([sys.executable, "src/scripts/validate_yaml.py", str(test_yaml)], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Validation successful" in result.stdout

def test_validator_invalid_missing_fields(tmp_path):
    test_yaml = tmp_path / "invalid_missing.yaml"
    # Missing required 'project' and 'signals' field
    data = {
        "test_steps": []
    }
    with open(test_yaml, "w") as f:
        yaml.dump(data, f)

    result = subprocess.run([sys.executable, "src/scripts/validate_yaml.py", str(test_yaml)], capture_output=True, text=True)
    assert result.returncode != 0
    assert "Validation failed" in result.stdout
    assert "'project' is a required property" in result.stdout

def test_validator_invalid_signal_type(tmp_path):
    test_yaml = tmp_path / "invalid_signal_case.yaml"
    data = {
        "project": "test",
        "signals": {
            "CLK": {"type": "invalid_type", "width": 1}
        },
        "test_steps": []
    }
    with open(test_yaml, "w") as f:
        yaml.dump(data, f)

    result = subprocess.run([sys.executable, "src/scripts/validate_yaml.py", str(test_yaml)], capture_output=True, text=True)
    assert result.returncode != 0
    assert "Validation failed" in result.stdout
    assert "'invalid_type' is not one of ['input', 'output', 'inout', 'clock']" in result.stdout

def test_validator_invalid_no_steps_or_cases(tmp_path):
    test_yaml = tmp_path / "invalid_no_steps.yaml"
    data = {
        "project": "test",
        "signals": {
            "CLK": {"type": "clock", "width": 1}
        }
    }
    with open(test_yaml, "w") as f:
        yaml.dump(data, f)

    result = subprocess.run([sys.executable, "src/scripts/validate_yaml.py", str(test_yaml)], capture_output=True, text=True)
    assert result.returncode != 0
    assert "Validation failed" in result.stdout
    assert "is not valid under any of the given schemas" in result.stdout
