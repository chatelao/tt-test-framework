import os
import subprocess
import yaml

def test_generator():
    test_yaml = "test/test_case.yaml"
    os.makedirs("test", exist_ok=True)

    data = {
        "project": "test",
        "signals": {"SIG": {"type": "input", "width": 1}},
        "test_steps": [{"name": "Step 1", "cycles": 1, "values": {"SIG": 1}}]
    }

    with open(test_yaml, "w") as f:
        yaml.dump(data, f)

    result = subprocess.run(["python", "src/scripts/generate_waveform.py", test_yaml], capture_output=True, text=True)
    assert result.returncode == 0
    assert os.path.exists("src/images/test_case.puml")

    with open("src/images/test_case.puml", "r") as f:
        content = f.read()
        assert "@startuml" in content
        assert "SIG is High" in content
        assert "@enduml" in content

    print("Test passed!")

if __name__ == "__main__":
    test_generator()
