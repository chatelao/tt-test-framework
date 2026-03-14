# Discarded Solutions

## 2-Bit Adder Verification Strategy (2025-05-23 11:00)

### Solution 2: Random Sampling (4 cycles)
- **Description**: Test only a few representative cases (e.g., all zeros, all ones, and two mixed cases).
- **Reasoning for Discarding**: While faster, it doesn't guarantee the correctness of the entire logic circuit.

### Solution 3: Sequential Input Sweeping (8 cycles)
- **Description**: Use a single test case with 8 cycles where inputs change at each clock edge.
- **Reasoning for Discarding**: Similar to Solution 1 but less explicit in naming each step's purpose in the YAML.

## Counter Verification Strategy (2025-05-23 10:00)

### Solution 2: Two full periods (8 cycles)
- **Description**: Eight separate test steps of 1 cycle each to verify the wrap-around behavior and periodicity.
- **Reasoning for Discarding**: While more thorough, it is somewhat redundant for a basic functional check and makes the YAML file unnecessarily long.

### Solution 3: Long observation (10 cycles)
- **Description**: A single test step with 10 cycles just to observe the waveform.
- **Reasoning for Discarding**: Does not provide per-cycle value verification, which is a key feature of the framework.
