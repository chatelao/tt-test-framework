# Discarded Solutions

## 10 Projects (project-id modulo 5 = 2) Verification Strategy (Test-IDs 3562-3617) (2026-03-16 11:30)

### Solution 2: Static Reset Only Verification
- **Description**: Only verify that the outputs are in a stable reset state.
- **Reasoning for Discarding**: Fails to verify any functional logic after reset, which is the primary goal of the test framework.

### Solution 3: Exhaustive Truth Table Testing
- **Description**: Test all possible input combinations (256 for 8-bit inputs).
- **Reasoning for Discarding**: Resulting timing diagrams would be unreadable and the YAML files would be excessively large.

## m6502 Microcontroller Verification Strategy (Test-ID 3528) (2026-03-15 13:57)

### Solution 2: NOP Fetch
- **Description**: Provide NOP instructions on the data bus and observe the address increment.
- **Reasoning for Discarding**: Requires several cycles of complex bus multiplexing which is too verbose for a simple functional test.

### Solution 3: Reset only
- **Description**: Verify outputs are stable during reset.
- **Reasoning for Discarding**: Does not verify that the CPU starts operation after reset.

## FH Joanneum TinyTapeout Verification Strategy (Test-ID 3531) (2026-03-15 13:57)

### Solution 2: SPI Echo
- **Description**: Send a byte via SPI and expect an echo or response.
- **Reasoning for Discarding**: Depends on the software loaded into the SERV core, which is not easily deterministic without full RTL simulation.

### Solution 3: GPIO Toggle
- **Description**: Set GPIO inputs and expect a change on outputs.
- **Reasoning for Discarding**: Similarly depends on the internal software state.

## OCP MXFP8 Streaming MAC Unit Verification Strategy (Test-ID 3990) (2026-03-15 08:58)

### Solution 2: Full 41-Cycle Sequence
- **Description**: Verify the entire 41-cycle standard protocol from initialization to output.
- **Reasoning for Discarding**: Resulting timing diagram would be overly dense and difficult to read without providing significantly more insight than the initial phase for a simple functional check.

### Solution 3: Reset Only
- **Description**: Verify only the reset state and initialization at Cycle 0.
- **Reasoning for Discarding**: Fails to demonstrate the FSM's progression through the multi-cycle configuration sequence.

## Handling of Project 3390 (mini mosbius) (2026-03-14 18:40)

### Solution 2: Implement basic test case for Project 3390
- **Description**: Create a minimal YAML test case for Project 3390 despite its analog nature.
- **Reasoning for Discarding**: Our framework is optimized for digital logic, and analog projects are explicitly skipped according to project memory and guidelines.

### Solution 3: Add to Planned section for ttsky25b
- **Description**: Keep Project 3390 in the roadmap but move it to a future shuttle section.
- **Reasoning for Discarding**: Unnecessary complexity as the current focus is entirely on completing the `ttihp26a` shuttle.

## tinyTapeVerilog_out Verification Strategy (Test-ID 3526) (2026-03-14 23:00)

### Solution 2: Reset only
- **Description**: Only verify that counter is 0 after reset.
- **Reasoning for Discarding**: Does not verify the primary functionality of the design (counting).

## Digital Lock Verification Strategy (Test-ID 3524) (2026-03-14 23:00)

### Solution 2: Exhaustive 4-bit search
- **Description**: Test all 16 possible 4-bit combinations.
- **Reasoning for Discarding**: Unnecessarily verbose for a simple combinational lock.

## Factory Test Verification Strategy (Test-ID 3487) (2026-03-14 23:00)

### Solution 2: Counter Only Test
- **Description**: Only test the incrementing counter behavior.
- **Reasoning for Discarding**: Fails to verify the pass-through logic which is half of the design's purpose.

## Chip ROM Verification Strategy (Test-ID 3486) (2026-03-14 23:00)

### Solution 2: Random Address Testing
- **Description**: Apply several random addresses and check if they pass through.
- **Reasoning for Discarding**: Less systematic than testing specific bit patterns like all-zeros and all-ones.

## Batch Rendering and WaveDrom Strategy (2026-03-14 18:30)

### Solution 1: Stick with PlantUML
- **Description**: Continue using PlantUML for waveform generation.
- **Reasoning for Discarding**: User explicitly requested the use of WaveDrom, which is better suited for the task.

### Solution 2: Environment Variable Overrides
- **Description**: Use environment variables to change the default output directories and suffixes.
- **Reasoning for Discarding**: Less explicit than command-line flags and harder to use for one-off variations in a loop.

### Solution 3: Dedicated Batch Script
- **Description**: Create a separate script specifically for this batch rendering task.
- **Reasoning for Discarding**: Introduces maintenance overhead and duplicates rendering logic instead of improving the core tool.

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

## 10 Additional TTIHP26a Projects (ID % 5 = 0) (2026-03-16 16:00)

### Solution 2: Generic Reset and Pattern Test
- **Description**: Use a uniform test template (reset + basic patterns) for all 10 projects regardless of their internal logic.
- **Reasoning for Discarding**: While faster, it fails to verify the specific functionality of complex designs like VGA controllers or debouncers.

### Solution 3: Automated Truth Table Generation
- **Description**: Attempt to automatically generate all possible input combinations for each project.
- **Reasoning for Discarding**: Impractical for sequential designs and results in excessively large YAML files that are difficult to review.
## 2026-03-15 19:28: Implementation of 10 test cases for ID % 5 = 2

- Solution 2: Too slow and error-prone compared to automated scripts.
- Solution 3: Inefficient as it retrieves many irrelevant projects.

## 10 Additional TTIHP26A Projects (ID % 5 = 1) (2026-03-16 17:15)

### Solution 2: Generic Reset and Pattern Test
- **Description**: Use a uniform test template for all 10 projects.
- **Reasoning for Discarding**: Fails to verify the specific functionality of diverse designs like multipliers or sequential chips.

### Solution 3: Exhaustive Truth Table Testing
- **Description**: Test all possible input combinations for all projects.
- **Reasoning for Discarding**: Impractical for complex and sequential designs, resulting in unreadable waveforms.

## Tiny Tapeout N Verification Strategy (Test-ID 3591) (2026-03-16 17:15)
### Solution 2: Reset Only
### Solution 3: Exhaustive Test

## TinyTapeoutTestProject Verification Strategy (Test-ID 3596) (2026-03-16 17:15)
### Solution 2: Reset Only
### Solution 3: Exhaustive Test

## just copy 4 not gates Verification Strategy (Test-ID 3601) (2026-03-16 17:15)
### Solution 2: Reset Only
### Solution 3: Exhaustive Test

## Tiny Tapeout Accumulator Verification Strategy (Test-ID 3606) (2026-03-16 17:15)
### Solution 2: Reset Only
### Solution 3: Exhaustive Test

## Chisel Async Test Verification Strategy (Test-ID 3656) (2026-03-16 17:15)
### Solution 2: Reset Only
### Solution 3: Random Patterns

## Cremedelcreme Verification Strategy (Test-ID 3701) (2026-03-16 17:15)
### Solution 2: Reset Only
### Solution 3: Exhaustive Test

## Scott's first Wokwi design Verification Strategy (Test-ID 3706) (2026-03-16 17:15)
### Solution 2: Reset Only
### Solution 3: Individual Bit Testing

## Tiny Tapeout chip Verification Strategy (Test-ID 3716) (2026-03-16 17:15)
### Solution 2: Reset Only
### Solution 3: Combinational-only testing

## fullAdder Verification Strategy (Test-ID 3731) (2026-03-16 17:15)
### Solution 2: Reset Only
### Solution 3: Partial Truth Table

## 8-bit SEM Floating-Point Multiplier Verification Strategy (Test-ID 3766) (2026-03-16 17:15)
### Solution 2: Reset Only
### Solution 3: Exhaustive Search
