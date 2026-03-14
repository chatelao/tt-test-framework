# Decisions

## YAML Validator Implementation (2025-05-22 11:00)

### Solution 1: Use `jsonschema` library (Chosen)
- **Description**: Utilize the standard `jsonschema` Python library to validate test data YAML files against a JSON schema.
- **Reasoning**: It is the industry standard for JSON/YAML validation, highly reliable, and easy to integrate once the schema is defined.

### Solution 2: Manual validation script
- **Description**: Write a custom Python script that iterates through the YAML structure and checks types/values manually.
- **Reasoning for Discarding**: This is error-prone and difficult to maintain as the schema evolves.

### Solution 3: Use `pydantic`
- **Description**: Define the schema using Pydantic models and parse the YAML into these models.
- **Reasoning for Discarding**: While powerful, it adds a heavier dependency and might be more complex than needed for simple schema validation in this context.

## Support for multiple test cases in one YAML file (2025-05-23 09:00)

### Solution 1: Root `test_cases` array with common `project`/`signals` (Chosen)
- **Description**: Introduce a `test_cases` field at the root, which is an array of objects, each containing a `name` and its own `test_steps`. Common `project` and `signals` definitions are shared.
- **Reasoning**: It allows sharing the project and signal definitions across multiple test cases within the same file, reducing redundancy while keeping the structure clean.
