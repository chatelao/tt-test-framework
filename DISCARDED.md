# Discarded Solutions

## GDS Test Verification Strategy (Test-ID 3697) (2026-03-14 14:10)

### Solution 2: Full 8-bit Truth Table (256 cycles)
- **Description**: Exhaustively test all combinations of the 8-bit input.
- **Reasoning for Discarding**: Unnecessarily long for verifying simple bit-level operations like inversion and pass-through.

## Full Adder Verification Strategy (Test-ID 3679) (2026-03-14 14:10)

### Solution 2: Representative Edge Cases (4 cycles)
- **Description**: Test only 0+0+0, 1+1+1, and two other cases.
- **Reasoning for Discarding**: While faster, it doesn't provide the same level of confidence as a full 8-cycle truth table.

## Doom? (Full Adder) Verification Strategy (Test-ID 3608) (2026-03-14 14:10)

### Solution 2: Representative Edge Cases (4 cycles)
- **Description**: Test only 0+0+0, 1+1+1, and two other cases.
- **Reasoning for Discarding**: While faster, it doesn't provide the same level of confidence as a full 8-cycle truth table.

## Counter Verification Strategy (Test-ID 3577) (2026-03-14 14:10)

### Solution 2: Full 18-bit Count Cycle
- **Description**: Run the counter through all 262,144 states.
- **Reasoning for Discarding**: Completely impractical for timing diagrams and basic functional verification.

## 74LS138 Verification Strategy (Test-ID 3625) (2026-03-14 14:10)

### Solution 2: Full 8-bit Truth Table (256 cycles)
- **Description**: Exhaustively test all combinations of the 8-bit input.
- **Reasoning for Discarding**: Unnecessarily long for verifying simple bit-level operations like inversion and pass-through.

## Implementation of Metadata and Source Field (2026-03-14 13:08)

### Solution 2: Root level only metadata object
- **Description**: Add a `metadata` object only at the root level of the YAML file.
- **Reasoning for Discarding**: Limits the ability to specify different sources for multiple test cases within the same file.

### Solution 3: Directly at root/case level without metadata object
- **Description**: Add a `source` field directly at the root level or inside `test_cases` items without wrapping it in a `metadata` object.
- **Reasoning for Discarding**: Less organized and makes it harder to add more metadata fields in the future without cluttering the top-level structure.

## 4-Bit Adder Verification Strategy (Test-ID 3657) (2025-05-23 13:00)

### Solution 2: Full Truth Table (256 cycles)
- **Description**: Exhaustively test all combinations of two 4-bit inputs.
- **Reasoning for Discarding**: Too many steps for a simple illustrative test case in YAML.

### Solution 3: Random Sampling (10 cycles)
- **Description**: Use 10 random pairs of inputs.
- **Reasoning for Discarding**: Less deterministic and may miss specific edge cases like carry-out.

## Counter Verification Strategy (2025-05-23 10:00)

### Solution 2: Two full periods (8 cycles)
- **Description**: Eight separate test steps of 1 cycle each to verify the wrap-around behavior and periodicity.
- **Reasoning for Discarding**: While more thorough, it is somewhat redundant for a basic functional check and makes the YAML file unnecessarily long.

### Solution 3: Long observation (10 cycles)
- **Description**: A single test step with 10 cycles just to observe the waveform.
- **Reasoning for Discarding**: Does not provide per-cycle value verification, which is a key feature of the framework.

## 2-Bit Adder Verification Strategy (2025-05-23 11:00)

### Solution 2: Random Sampling (4 cycles)
- **Description**: Test only a few representative cases (e.g., all zeros, all ones, and two mixed cases).
- **Reasoning for Discarding**: While faster, it doesn't guarantee the correctness of the entire logic circuit.

### Solution 3: Sequential Input Sweeping (8 cycles)
- **Description**: Use a single test case with 8 cycles where inputs change at each clock edge.
- **Reasoning for Discarding**: Similar to Solution 1 but less explicit in naming each step's purpose in the YAML.
