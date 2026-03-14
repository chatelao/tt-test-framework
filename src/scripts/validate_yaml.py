import yaml
import sys
import os
from jsonschema import validate, ValidationError

def validate_yaml(data_path, schema_path):
    with open(schema_path, 'r') as f:
        schema = yaml.safe_load(f)

    with open(data_path, 'r') as f:
        data = yaml.safe_load(f)

    try:
        validate(instance=data, schema=schema)
        print(f"Validation successful for {data_path}")
        return True
    except ValidationError as e:
        print(f"Validation failed for {data_path}")
        print(f"Error: {e.message}")
        print(f"Path: {list(e.path)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_yaml.py <input_yaml> [schema_yaml]")
        sys.exit(1)

    input_yaml = sys.argv[1]
    schema_yaml = sys.argv[2] if len(sys.argv) > 2 else "src/schema/test_steps.yaml"

    if not validate_yaml(input_yaml, schema_yaml):
        sys.exit(1)
