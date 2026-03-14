# Decisions

## Implementation of Metadata and Source Field (2026-03-14 13:08)

### Solution 1: Root and test_cases level metadata object (Chosen)
- **Description**: Add a `metadata` object that can contain a `source` field at both the root level (global) and within each test case in `test_cases`.
- **Reasoning**: Provides flexibility to specify a source for the entire file or for individual test cases if they come from different sources.

## Project Structure Reorganization (2025-05-23 09:00)

### Solution 1: Move images to /images and .puml to /src/puml (Chosen)
- **Description**: Relocate generated PNG images to the root `/images` directory and PlantUML source files to `/src/puml`.
- **Reasoning**: Adheres to the user's specific request for better organization and separation of source files from generated artifacts.

### Solution 2: Move all artifacts to a single /artifacts directory
- **Description**: Consolidate all generated files into a single root-level directory.
- **Reasoning for Discarding**: Does not follow the specific organizational preference requested by the user.

### Solution 3: Use a flat structure in /src
- **Description**: Keep all files in the root of `/src`.
- **Reasoning for Discarding**: This would clutter the source directory and make it harder to distinguish between logic, data, and artifacts.

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

## Support for Multiple Test Cases (2025-05-22 14:00)

### Solution 1: Nested `test_cases` array (Chosen)
- **Description**: Introduce a `test_cases` key at the root, which is an array of objects. Each object contains a `name` and its own `test_steps` array.
- **Reasoning**: This provides a clear, named structure for multiple sequences while allowing them to share the top-level `project` and `signals` definitions.

### Solution 2: Dictionary-based `test_steps`
- **Description**: Modify `test_steps` to optionally be a dictionary where keys are case names and values are the step arrays.
- **Reasoning for Discarding**: It makes the schema for `test_steps` more complex (union type) and is less explicit than a dedicated `test_cases` field.

### Solution 3: Multi-document YAML
- **Description**: Use YAML's `---` separator to define multiple complete test documents within a single file.
- **Reasoning for Discarding**: This would require duplicating `project` and `signals` definitions in every document or implementing a complex merging logic.

## 2-Bit Adder Verification Strategy (2025-05-23 11:00)

### Solution 1: Full Truth Table (8 cycles) (Chosen)
- **Description**: Define eight test steps to cover all combinations of inputs A, B, and Cin.
- **Reasoning**: This provides comprehensive verification of the combinational logic for a simple 2-bit (full) adder.

### Solution 2: Random Sampling (4 cycles)
- **Description**: Test only a few representative cases (e.g., all zeros, all ones, and two mixed cases).
- **Reasoning for Discarding**: While faster, it doesn't guarantee the correctness of the entire logic circuit.

### Solution 3: Sequential Input Sweeping (8 cycles)
- **Description**: Use a single test case with 8 cycles where inputs change at each clock edge.
- **Reasoning for Discarding**: Similar to Solution 1 but less explicit in naming each step's purpose in the YAML.

## Counter Verification Strategy (2025-05-23 10:00)

### Solution 1: One full period (4 cycles) (Chosen)
- **Description**: Define four test steps, each 1 cycle long, to verify the sequence 1, 2, 3, 4.
- **Reasoning**: This is the most efficient way to confirm the core functionality of the counter as described in the specifications.

## 2-Bit Adder Verification Strategy (Test-ID 3564) (2025-05-23 12:00)

### Solution 1: Full Truth Table (16 cycles) (Chosen)
- **Description**: Define 16 test steps to cover all combinations of two 2-bit inputs.
- **Reasoning**: Provides exhaustive verification of the combinational logic for the 2-bit adder.

### Solution 2: Representative Cases (8 cycles)
- **Description**: Test only a subset of inputs (e.g., all zeros, all ones, and mixed values).
- **Reasoning for Discarding**: Does not guarantee full correctness of the circuit, though faster to define.

### Solution 3: Randomized Input Testing
- **Description**: Generate random pairs of 2-bit numbers and verify the sum.
- **Reasoning for Discarding**: Difficult to implement in a static YAML-based test framework without a script to pre-calculate results.
