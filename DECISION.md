# Decisions

## Add Novelty Column to TTIHP26A Projects Overview (2026-03-15 15:45)

### Solution 1: Size-based Heuristic (Chosen)
- **Description**: Implement the "Novelty" column using a T-shirt size-based heuristic (S: ⭐, M: ⭐⭐, L: ⭐⭐⭐, XL: ⭐⭐⭐⭐, XXL/XXXL: ⭐⭐⭐⭐⭐) to provide a deterministic 1-5 star rating.
- **Reasoning**: This provides a consistent and automated way to fill the novelty rating based on project complexity (area/tiles), which is a good proxy for "novelty" in the context of TinyTapeout projects when specific ratings are not available.

## TTIHP26A Projects Overview Generation (2026-03-16 11:30)

### Solution 1: Automated Scraping and Generation (Chosen)
- **Description**: Use a Playwright-based script to scrape the TinyTapeout website for project metadata and combine it with local file checks to generate the markdown table.
- **Reasoning**: This is the most accurate and scalable way to handle over 100 projects, ensuring that "Tiles" data (not available locally) and project names are up-to-date.

### Solution 2: Manual Table Creation
- **Description**: Manually gather data for each project and write the markdown table.
- **Reasoning for Discarding**: Extremely time-consuming and prone to human error given the large number of projects.

### Solution 3: Static Metadata File
- **Description**: Create a static JSON/YAML file with all project metadata and use a simple script to render the table.
- **Reasoning for Discarding**: Requires manual maintenance of the metadata file; automated scraping is superior for initial creation and future updates.

## Next 10 TTIHP26a Projects Verification Strategy (Test-IDs 3548-3559) (2026-03-16 10:00)

### Solution 1: Targeted Functional Verification (Chosen)
- **Description**: Implement simple functional test cases for each of the 10 projects (Full Adder, Rasterizer, Counter, Clock Divider, Letter Display, etc.) based on their specific logic and pinouts.
- **Reasoning**: This provides meaningful verification for a diverse set of projects ranging from simple combinational logic to complex VGA and sequential designs.

## m6502 Microcontroller Verification Strategy (Test-ID 3528) (2026-03-15 13:57)

### Solution 1: Bus Initialization (Chosen)
- **Description**: Verify that the PHI1/PHI2 clocks start toggling and the R/W signal is initialized to Read after reset.
- **Reasoning**: Confirms the basic operation of the CPU's internal clock generator and the initial state of the memory interface.

### Solution 2: NOP Fetch
- **Description**: Provide NOP instructions on the data bus and observe the address increment.
- **Reasoning for Discarding**: Requires several cycles of complex bus multiplexing which is too verbose for a simple functional test.

### Solution 3: Reset only
- **Description**: Verify outputs are stable during reset.
- **Reasoning for Discarding**: Does not verify that the CPU starts operation after reset.

## FH Joanneum TinyTapeout Verification Strategy (Test-ID 3531) (2026-03-15 13:57)

### Solution 1: Reset State (Chosen)
- **Description**: Verify that SPI and GPIO outputs are in their default (likely zero or high-Z) state after reset.
- **Reasoning**: A safe and necessary sanity check for an SoC to ensure it doesn't drive unexpected values on boot.

### Solution 2: SPI Echo
- **Description**: Send a byte via SPI and expect an echo or response.
- **Reasoning for Discarding**: Depends on the software loaded into the SERV core, which is not easily deterministic without full RTL simulation.

### Solution 3: GPIO Toggle
- **Description**: Set GPIO inputs and expect a change on outputs.
- **Reasoning for Discarding**: Similarly depends on the internal software state.

## Piggybag Verification Strategy (Test-ID 3533) (2026-03-15 13:57)

### Solution 1: Pattern Testing (Chosen)
- **Description**: Test various input patterns to verify the 1:1 or simple logic mapping in this Wokwi project.
- **Reasoning**: Appropriate for simple Wokwi designs with direct pin mappings.

## 6 Bit Roulette Verification Strategy (Test-ID 3537) (2026-03-15 13:57)

### Solution 1: Reset and Idle (Chosen)
- **Description**: Verify the LED segments (outputs) are in a known state after reset.
- **Reasoning**: Confirms the sequential logic of the roulette game is correctly initialized.

## secretNo Verification Strategy (Test-ID 3539) (2026-03-15 13:57)

### Solution 1: Logic Verification (Chosen)
- **Description**: Test the 4-bit input combinations to verify the unlocking logic.
- **Reasoning**: Directly tests the core functional requirement of this "secret number" project.

## My first Wokwi design Verification Strategy (Test-ID 3540) (2026-03-15 13:57)

### Solution 1: Code Verification (Chosen)
- **Description**: Apply the "secret code" via inputs and verify the 7-segment output shows the intended letter.
- **Reasoning**: Verifies the unique functional goal of the project.

## VGABlock Verification Strategy (Test-ID 3542) (2026-03-15 13:57)

### Solution 1: Sync Signal Verification (Chosen)
- **Description**: Verify HSync and VSync initialization and initial toggling.
- **Reasoning**: Standard verification approach for VGA projects in this framework.

## SotaSoC Verification Strategy (Test-ID 3543) (2026-03-15 13:57)

### Solution 1: Reset State (Chosen)
- **Description**: Verify that UART and SPI outputs are in their expected idle state (e.g., UART_TX high) after reset.
- **Reasoning**: Confirms the complex SoC's peripherals are correctly initialized and the reset signal propagates as expected.

## Tiny Ape Out Verification Strategy (Test-ID 3545) (2026-03-15 13:57)

### Solution 1: Pattern Testing (Chosen)
- **Description**: Test various input patterns to verify the logic mapping in this Wokwi project.
- **Reasoning**: Appropriate for simple Wokwi designs with direct pin mappings.

## tiny-tapeout-workshop-result Verification Strategy (Test-ID 3547) (2026-03-15 13:57)

### Solution 1: Enable and Mux Verification (Chosen)
- **Description**: Verify that outputs toggle when enabled and remain stable when disabled.
- **Reasoning**: Directly tests the control logic and multiplexing described in the project's description.

## OCP MXFP8 Streaming MAC Unit Verification Strategy (Test-ID 3990) (2026-03-15 08:58)

### Solution 1: Protocol Initial Phase (Chosen)
- **Description**: Verify the initial 5 cycles of the protocol: Metadata load, Scale A load, Scale B load, and the start of the streaming phase.
- **Reasoning**: This confirms the FSM correctly transitions through the configuration states into the streaming state as documented, providing a clear and readable timing diagram.

## Handling of Project 3390 (mini mosbius) (2026-03-14 18:40)

### Solution 1: Skip Project 3390 (Chosen)
- **Description**: Skip the project because it is designated as "Analog" and belongs to the `ttsky25b` shuttle, which is outside the current digital verification scope for `ttihp26a`.
- **Reasoning**: This adheres to the project policy of excluding analog designs and focusing on the primary `ttihp26a` shuttle for now.

### Solution 2: Implement basic test case for Project 3390
- **Description**: Create a minimal YAML test case for Project 3390 despite its analog nature.
- **Reasoning for Discarding**: Our framework is optimized for digital logic, and analog projects are explicitly skipped according to project memory and guidelines.

### Solution 3: Add to Planned section for ttsky25b
- **Description**: Keep Project 3390 in the roadmap but move it to a future shuttle section.
- **Reasoning for Discarding**: Unnecessary complexity as the current focus is entirely on completing the `ttihp26a` shuttle.

## Verification Strategy for 12 TTIHP26a Projects (2026-03-14 18:00)

### Solution 1: Manual exploration and YAML creation (Chosen)
- **Description**: Implement each test case manually by exploring the project's repository to understand its logic and pinout, then create meaningful test steps in YAML.
- **Reasoning**: This ensures high-quality and accurate test data that accurately reflects the intended behavior of each project, especially for complex designs like SoCs and FPGAs.

## tinyTapeVerilog_out Verification Strategy (Test-ID 3526) (2026-03-14 23:00)

### Solution 1: Counter Sequence (Chosen)
- **Description**: Observe the counter incrementing over several cycles after reset and verify enable logic.
- **Reasoning**: Verifies the core functional block and confirms that both reset and enable signals work as expected.

### Solution 2: Reset only
- **Description**: Only verify that counter is 0 after reset.
- **Reasoning for Discarding**: Does not verify the primary functionality of the design (counting).

## Digital Lock Verification Strategy (Test-ID 3524) (2026-03-14 23:00)

### Solution 1: Code Verification (Chosen)
- **Description**: Test the unlock code (1011) and representative near-misses (Easter eggs 1010, 1001, 0011).
- **Reasoning**: Provides targeted verification of the design's specific functional requirements and edge cases.

### Solution 2: Exhaustive 4-bit search
- **Description**: Test all 16 possible 4-bit combinations.
- **Reasoning for Discarding**: Unnecessarily verbose for a simple combinational lock.

## Factory Test Verification Strategy (Test-ID 3487) (2026-03-14 23:00)

### Solution 1: Mode Switching (Chosen)
- **Description**: Test both pass-through mode (ui_in[0]=0) and counter mode (ui_in[0]=1) with internal reset synchronization.
- **Reasoning**: Comprehensive check of both operational modes and the control logic that selects between them.

### Solution 2: Counter Only Test
- **Description**: Only test the incrementing counter behavior.
- **Reasoning for Discarding**: Fails to verify the pass-through logic which is half of the design's purpose.

## Chip ROM Verification Strategy (Test-ID 3486) (2026-03-14 23:00)

### Solution 1: Pass-through Verification (Chosen)
- **Description**: Verify that the output matches the input as per the placeholder Verilog implementation.
- **Reasoning**: Since the actual ROM is generated later, verifying the wrapper's pass-through logic is the only deterministic test available at this stage.

### Solution 2: Random Address Testing
- **Description**: Apply several random addresses and check if they pass through.
- **Reasoning for Discarding**: Less systematic than testing specific bit patterns like all-zeros and all-ones.

## Batch Rendering and WaveDrom Strategy (2026-03-14 18:30)

### Solution 1: WaveDrom for Waveform Generation (Chosen)
- **Description**: Use the WaveDrom engine (via the `wavedrom` Python library) to generate waveforms instead of PlantUML.
- **Reasoning**: WaveDrom is specifically designed for digital timing diagrams and provides a more industry-standard look and feel for these types of projects.

### Solution 2: Parameterized Script with `argparse` (Chosen)
- **Description**: Enhance `generate_waveform.py` to accept `--outdir` and `--suffix` arguments.
- **Reasoning**: Provides a clean, flexible interface for batch processing and custom naming without breaking existing workflows.

### Solution 2: Environment Variable Overrides
- **Description**: Use environment variables to change the default output directories and suffixes.
- **Reasoning for Discarding**: Less explicit than command-line flags and harder to use for one-off variations in a loop.

### Solution 3: Dedicated Batch Script
- **Description**: Create a separate script specifically for this batch rendering task.
- **Reasoning for Discarding**: Introduces maintenance overhead and duplicates rendering logic instead of improving the core tool.

## 1-bit Full Adder Verification Strategy (Test-ID 3614) (2026-03-14 16:30)

### Solution 1: Full Truth Table (8 cycles) (Chosen)
- **Description**: Define eight test steps to cover all combinations of inputs A, B, and Carry.
- **Reasoning**: Provides comprehensive verification of the combinational logic for the 1-bit full adder.

### Solution 2: Pattern Testing (4 cycles)
- **Description**: Test only representative cases like 0+0+0, 1+1+0, 1+1+1.
- **Reasoning for Discarding**: Does not guarantee full correctness of all logic branches.

### Solution 3: Sequential sweeping
- **Description**: Sweep through inputs in a single multi-cycle test case.
- **Reasoning for Discarding**: Less descriptive than individual steps.

## Logic Gates Verification Strategy (Test-ID 3711) (2026-03-14 16:30)

### Solution 1: Pattern Testing (4 cycles) (Chosen)
- **Description**: Test various input combinations to verify NAND and other logic gate outputs.
- **Reasoning**: Efficiently confirms the basic logic gate operations implemented in the Wokwi project.

### Solution 2: Full Truth Table
- **Description**: Test all 64 combinations of the 6 inputs.
- **Reasoning for Discarding**: Too verbose for a simple logic gate test.

### Solution 3: Random Sampling
- **Description**: Test a few random input patterns.
- **Reasoning for Discarding**: May miss specific logic transitions.

## 7-Segment BCD Verification Strategy (Test-ID 3684) (2026-03-14 16:30)

### Solution 1: Representative Digits (5 cycles) (Chosen)
- **Description**: Test values 0, 1, 2, 8, 9 to verify the BCD to 7-segment decoding logic.
- **Reasoning**: Covers the most distinctive patterns for 7-segment displays without being exhaustive.

### Solution 2: Full 0-9 sequence
- **Description**: Test every digit from 0 to 9.
- **Reasoning for Discarding**: Slightly redundant for verifying the core functionality.

### Solution 3: Pass-through testing
- **Description**: Check if inputs are just passed to outputs.
- **Reasoning for Discarding**: Incorrect as the project implements decoding logic.

## Copenhagen Workshop Verification Strategy (Test-ID 3720) (2026-03-14 16:30)

### Solution 1: Logic Verification (4 cycles) (Chosen)
- **Description**: Test the AND, OR, NAND, and XOR gates mapped to the outputs.
- **Reasoning**: Directly verifies the simple combinational logic components found in the Wokwi diagram.

### Solution 2: Pattern Testing
- **Description**: Test all zeros and all ones.
- **Reasoning for Discarding**: Insufficient to distinguish between different gate types.

### Solution 3: Random Sampling
- **Description**: Use random inputs.
- **Reasoning for Discarding**: Unreliable for specific logic verification.

## TeenySPU Verification Strategy (Test-ID 3665) (2026-03-14 16:30)

### Solution 1: Initial Reset and NOP (5 cycles) (Chosen)
- **Description**: Verify the processor stays in a neutral state after reset with no-operation instructions.
- **Reasoning**: Confirms basic sanity of the sequential logic and reset behavior for the spatial processing unit.

### Solution 2: Basic Addition Test
- **Description**: Execute a simple addition instruction.
- **Reasoning for Discarding**: Requires more complex setup of opcode and operand signals than necessary for a basic functional test.

### Solution 3: Loop Verification
- **Description**: Run a small program loop.
- **Reasoning for Discarding**: Too complex for a simple YAML-based waveform generation.

## Silly Mixer Verification Strategy (Test-ID 3764) (2026-03-14 16:30)

### Solution 1: Pattern Testing (4 cycles) (Chosen)
- **Description**: Test various input patterns to verify the mixing/summing logic.
- **Reasoning**: Provides a quick check of the project's ability to process and output data based on inputs.

### Solution 2: Full Summation Test
- **Description**: Exhaustively test multiple input pairs.
- **Reasoning for Discarding**: Complexity of the internal mixer logic makes exhaustive testing difficult without more detail.

### Solution 3: Zero Input Test
- **Description**: Verify that zero inputs result in zero output.
- **Reasoning for Discarding**: Too basic to confirm anything beyond simple connection.

## VGA Silly Dog Verification Strategy (Test-ID 3512) (2026-03-14 16:30)

### Solution 1: Sync Signal Verification (10 cycles) (Chosen)
- **Description**: Verify that HSync and VSync signals are initialized correctly after reset.
- **Reasoning**: Most reliable way to test a VGA project in a short simulation window without full frame rendering.

### Solution 2: Pixel Data Testing
- **Description**: Check RGB values at specific coordinates.
- **Reasoning for Discarding**: Coordinates depend on internal counters that take thousands of cycles to reach interesting areas.

### Solution 3: Clock Swapping
- **Description**: Test with different clock frequencies.
- **Reasoning for Discarding**: Not supported by the current YAML framework's timing diagram generator.

## Paafu Verification Strategy (Test-ID 3685) (2026-03-14 16:30)

### Solution 1: Pattern Testing (4 cycles) (Chosen)
- **Description**: Test alternating inputs to verify the 1:1 or simple logic mapping.
- **Reasoning**: Sufficient for a very simple project with only one active input and output.

### Solution 2: Static Input Test
- **Description**: Hold input at 1.
- **Reasoning for Discarding**: Doesn't verify signal propagation or transitions.

### Solution 3: Random Sampling
- **Description**: Use random input patterns.
- **Reasoning for Discarding**: Overkill for such a simple design.

## Moving Average Filter Verification Strategy (Test-ID 3666) (2026-03-14 16:30)

### Solution 1: Pass-Through Mode (4 cycles) (Chosen)
- **Description**: Set number of taps to 1 and verify that data_in is passed to result_out.
- **Reasoning**: Simplest way to verify the entire data path and control signals (ready/valid) in a short sequence.

### Solution 2: Small Average (8 cycles)
- **Description**: Set taps to 2 and send a few samples.
- **Reasoning for Discarding**: Requires more cycles to observe the first valid result, making the waveform harder to read.

### Solution 3: Reset Verification
- **Description**: Only test that the busy signal goes low after reset.
- **Reasoning for Discarding**: Doesn't verify the core functional logic of the filter.

## Mein Hund Gniesbert Verification Strategy (Test-ID 3551) (2026-03-14 16:30)

### Solution 1: "Number 3" Verification (4 cycles) (Chosen)
- **Description**: Test inputs that sum to 3 and verify the specific output pattern described.
- **Reasoning**: Directly tests the unique functional requirement of this "3-only" adder.

### Solution 2: Zero Test
- **Description**: Check if 0+0 results in zero.
- **Reasoning for Discarding**: The project description suggests it might only work for 3, so zero might not be as interesting.

### Solution 3: Exhaustive 3-bit Test
- **Description**: Test all combinations of the 3-bit input.
- **Reasoning for Discarding**: Less focused on the "Number 3" theme.

## Hello GDS Verification Strategy (Test-ID 3704) (2026-03-14 16:30)

### Solution 1: Basic Toggling (5 cycles) (Chosen)
- **Description**: Verify that internal flops and outputs toggle or remain stable as expected under a clock.
- **Reasoning**: Confirms that the sequential elements and basic gate logic in this "random" project are active.

### Solution 2: Reset Test
- **Description**: Only verify the reset state.
- **Reasoning for Discarding**: Doesn't prove the design works once out of reset.

### Solution 3: Static Pattern Test
- **Description**: Apply static inputs and check outputs.
- **Reasoning for Discarding**: The design has internal state (flops), so a sequential test is more appropriate.

## Systolic Array Verification Strategy (Test-ID 3647) (2026-03-14 16:30)

### Solution 1: Initial Reset and Idle (5 cycles) (Chosen)
- **Description**: Verify that the array is correctly initialized and remains idle when no data is valid.
- **Reasoning**: Essential first step for complex sequential designs like systolic arrays to ensure the control logic starts correctly.

### Solution 2: Single MAC operation
- **Description**: Feed one set of data and observe one multiplication-accumulation.
- **Reasoning for Discarding**: Too many cycles and complex signal sequences (JTAG/Data Mode) for a basic YAML test.

### Solution 3: JTAG IDCODE Read
- **Description**: Verify JTAG interface by reading the IDCODE.
- **Reasoning for Discarding**: Focuses on JTAG rather than the core systolic array logic.

## GDS Test Verification Strategy (Test-ID 3697) (2026-03-14 14:10)

### Solution 1: Pattern Testing (4 cycles) (Chosen)
- **Description**: Test all zeros, all ones, and alternating bit patterns.
- **Reasoning**: Efficiently verifies the observed signal inversion for the lower 4 bits and pass-through for the upper 4 bits.

## Full Adder Verification Strategy (Test-ID 3679) (2026-03-14 14:10)

### Solution 1: Full Truth Table (8 cycles) (Chosen)
- **Description**: Define eight test steps to cover all combinations of inputs A, B, and Cin.
- **Reasoning**: Provides comprehensive verification of the combinational logic for the full adder.

## Doom? (Full Adder) Verification Strategy (Test-ID 3608) (2026-03-14 14:10)

### Solution 1: Full Truth Table (8 cycles) (Chosen)
- **Description**: Define eight test steps to cover all combinations of inputs A, B, and Cin.
- **Reasoning**: Provides comprehensive verification of the combinational logic for the full adder.

## Counter Verification Strategy (Test-ID 3577) (2026-03-14 14:10)

### Solution 1: Initial State Verification (5 cycles) (Chosen)
- **Description**: Verify the initial state of the counter remains zero for the first few cycles.
- **Reasoning**: Confirm that the counter starts at zero and remains there for a short duration, which is expected for a large 18-bit ripple counter at low cycle counts.

## 74LS138 Verification Strategy (Test-ID 3625) (2026-03-14 14:10)

### Solution 1: Pattern Testing (4 cycles) (Chosen)
- **Description**: Test all zeros, all ones, and alternating bit patterns.
- **Reasoning**: Efficiently verifies the observed signal inversion for the lower 4 bits and pass-through for the upper 4 bits.

## TinyTapeout logic gate test Verification Strategy (Test-ID 3603) (2026-03-14 17:00)

### Solution 1: Basic Logic Test (4 cycles) (Chosen)
- **Description**: Verify OR and XOR gates by toggling inputs.
- **Reasoning**: Directly confirms the combinational logic for the gates identified in the Wokwi diagram.

## Verilog ring oscillator V2 Verification Strategy (Test-ID 3737) (2026-03-14 17:00)

### Solution 1: Initial Reset (5 cycles) (Chosen)
- **Description**: Verify initial state after reset.
- **Reasoning**: Ring oscillators are hard to simulate deterministically; verifying reset behavior is a safe starting point.

## VoGAl Verification Strategy (Test-ID 3957) (2026-03-14 17:00)

### Solution 1: Sync Signal Verification (10 cycles) (Chosen)
- **Description**: Verify HSync and VSync initialization.
- **Reasoning**: Standard verification approach for VGA projects in this framework.

## Yet another VGA tinytapeout Verification Strategy (Test-ID 3638) (2026-03-14 17:00)

### Solution 1: Sync Signal Verification (10 cycles) (Chosen)
- **Description**: Verify HSync and VSync initialization.
- **Reasoning**: Standard verification approach for VGA projects in this framework.

## Yturkeri_Mytinytapeout Verification Strategy (Test-ID 3556) (2026-03-14 17:00)

### Solution 1: Pattern Testing (4 cycles) (Chosen)
- **Description**: Test various input patterns to verify the 1:1 or simple logic mapping.
- **Reasoning**: Sufficient for a very simple logic gate project.

## lriglooCs-first-Wokwi-design Verification Strategy (Test-ID 3587) (2026-03-14 17:00)

### Solution 1: Pattern Testing (4 cycles) (Chosen)
- **Description**: Test various input patterns to verify the 1:1 mapping.
- **Reasoning**: Matches the simple Wokwi diagram for this "8-bit-adder" which appears to be a pass-through.

## random stuff Verification Strategy (Test-ID 3581) (2026-03-14 17:00)

### Solution 1: Pattern Testing (4 cycles) (Chosen)
- **Description**: Test various input patterns to verify the logic.
- **Reasoning**: Sufficient for a simple Wokwi project.

## smolCPU Verification Strategy (Test-ID 3970) (2026-03-14 17:00)

### Solution 1: Reset and NOP (5 cycles) (Chosen)
- **Description**: Verify CPU state after reset.
- **Reasoning**: Confirms sanity of sequential logic and reset state.

## sree Verification Strategy (Test-ID 3724) (2026-03-14 17:00)

### Solution 1: Initial State (5 cycles) (Chosen)
- **Description**: Verify outputs remain zero or stable after reset.
- **Reasoning**: Basic functional check for a simple Wokwi design.

## tinytapout_test Verification Strategy (Test-ID 3538) (2026-03-14 17:00)

### Solution 1: Logic Test (4 cycles) (Chosen)
- **Description**: Verify AND, NAND, and OR gates and clock dividers.
- **Reasoning**: Covers the functional blocks described in the project pinout.

## test hard macro Verification Strategy (Test-ID 3759) (2026-03-14 17:00)

### Solution 1: 4-bit Adder Test (5 cycles) (Chosen)
- **Description**: Test representative cases for the 4-bit adder.
- **Reasoning**: Directly verifies the core functional logic of the hard macro.

## tinytapeout Verification Strategy (Test-ID 3609) (2026-03-14 17:00)

### Solution 1: Pattern Testing (4 cycles) (Chosen)
- **Description**: Test various input patterns.
- **Reasoning**: Sufficient for a simple Wokwi design.

## tinytapeout_henningp_2bin_to_4bit_decoder Verification Strategy (Test-ID 3707) (2026-03-14 17:00)

### Solution 1: Decoder Truth Table (4 cycles) (Chosen)
- **Description**: Test all 4 combinations of the 2-bit input.
- **Reasoning**: Fully verifies the 2-to-4 decoder logic.

## tt-verilog Verification Strategy (Test-ID 3618) (2026-03-14 17:00)

### Solution 1: Reset State (5 cycles) (Chosen)
- **Description**: Verify I2C signals (SDA/SCL) are in correct state after reset.
- **Reasoning**: Safe check for an I2C-related project.

## vga_ca Verification Strategy (Test-ID 3975) (2026-03-14 17:00)

### Solution 1: Sync Signal Verification (10 cycles) (Chosen)
- **Description**: Verify HSync and VSync initialization.
- **Reasoning**: Standard verification approach for VGA projects.

## Johnson counter Verification Strategy (Test-ID 3726) (2026-03-14 17:00)

### Solution 1: Counter Sequence (8 cycles) (Chosen)
- **Description**: Observe the Johnson counter sequence after reset.
- **Reasoning**: Verifies the unique sequence of this counter type.

## ttip-test Verification Strategy (Test-ID 3662) (2026-03-14 17:00)

### Solution 1: Pattern Testing (4 cycles) (Chosen)
- **Description**: Verify signal propagation through the counter project.
- **Reasoning**: Simple functional check.

## I2C to SPI Bridge Verification Strategy (Test-ID 3682) (2026-03-14 17:00)

### Solution 1: Reset and Idle (5 cycles) (Chosen)
- **Description**: Verify bridge is idle after reset.
- **Reasoning**: Essential sanity check for a communication bridge.

## Herald Verification Strategy (Test-ID 3534) (2026-03-14 17:00)

### Solution 1: Reset State (5 cycles) (Chosen)
- **Description**: Verify DSP core is idle after reset.
- **Reasoning**: Confirms the sequential logic is correctly initialized.

## FH Joanneum TinyTapeout Verification Strategy (Test-ID 3565) (2026-03-14 17:00)

### Solution 1: Reset State (5 cycles) (Chosen)
- **Description**: Verify SoC pins are in expected state after reset.
- **Reasoning**: Basic verification for a complex RISC-V SoC.

## Implementation of Metadata and Source Field (2026-03-14 13:08)

### Solution 1: Root and test_cases level metadata object (Chosen)
- **Description**: Add a `metadata` object that can contain a `source` field at both the root level (global) and within each test case in `test_cases`.
- **Reasoning**: Provides flexibility to specify a source for the entire file or for individual test cases if they come from different sources.

## Project Structure Reorganization (2025-05-23 09:00)

### Solution 1: Move waveforms to /waveforms and .puml to /src/puml (Chosen)
- **Description**: Relocate generated PNG waveforms to the root `/waveforms` directory and PlantUML source files to `/src/puml`.
- **Reasoning**: Adheres to the user's specific request for better organization and separation of source files from generated artifacts.

### Solution 2: Move all artifacts to a single /artifacts directory
- **Description**: Consolidate all generated files into a single root-level directory.
- **Reasoning for Discarding**: Does not follow the specific organizational preference requested by the user.

### Solution 3: Use a flat structure in /src
- **Description**: Keep all files in the root of `/src`.
- **Reasoning for Discarding**: This would clutter the source directory and make it harder to distinguish between logic, data, and artifacts.

## 2-Bit Adder Verification Strategy (Test-ID 3723) (2025-05-23 13:20)

### Solution 1: Pass-through Testing (4 cycles) (Chosen)
- **Description**: Test various patterns to ensure 1:1 input to output mapping.
- **Reasoning**: Matches the simple OR-gate-based pass-through logic seen in the project's Wokwi diagram.

## 7 Segment Number Viewer Verification (Test-ID 3723) (2025-05-23 13:20)

### Solution 1: Pass-through Testing (4 cycles) (Chosen)
- **Description**: Test various patterns to ensure 1:1 input to output mapping.
- **Reasoning**: Matches the simple OR-gate-based pass-through logic seen in the project's Wokwi diagram.

## 7 Segment Binary Viewer Verification (Test-ID 3674) (2025-05-23 13:10)

### Solution 1: Pattern Testing (4 cycles) (Chosen)
- **Description**: Test all zeros, all ones, and alternating bit patterns.
- **Reasoning**: Efficiently verifies the observed signal inversion in the Wokwi diagram for the lower 4 bits.

## 4-Bit Adder Verification Strategy (Test-ID 3657) (2025-05-23 13:00)

### Solution 1: Representative Edge Cases (5 cycles) (Chosen)
- **Description**: Test 0+0, 1+1, 15+1 (carry out), 15+15 (max value), and 5+10.
- **Reasoning**: Provides good coverage of typical and edge cases for a 4-bit adder without the 256 steps required for a full truth table.

### Solution 2: Full Truth Table (256 cycles)
- **Description**: Exhaustively test all combinations of two 4-bit inputs.
- **Reasoning for Discarding**: Too many steps for a simple illustrative test case in YAML.

### Solution 3: Random Sampling (10 cycles)
- **Description**: Use 10 random pairs of inputs.
- **Reasoning for Discarding**: Less deterministic and may miss specific edge cases like carry-out.

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

## 2026-03-14 12:00:00 - Implement Batch 1 of 4 (Projects 3489, 3491, 3492, 3493, 3494)

### Solution 1: Implement Batch 1 (Chosen)
Implement test data for projects 3489, 3491, 3492, 3493, and 3494 based on their info.yaml research.

## 2026-03-14 12:05:00 - Implement Batch 2 of 4 (Projects 3495, 3497, 3498, 3503, 3504)

### Solution 1: Implement Batch 2 (Chosen)
Implement test data for projects 3495, 3497, 3498, 3503, and 3504. Project 3497 is a silicon art project with simple XOR logic. 3498 is an MBIST controller. 3503 and 3504 are Wokwi-based projects.

## 2026-03-14 12:10:00 - Implement Batch 3 of 4 (Projects 3506, 3505, 3508, 3507, 3510)

### Solution 1: Implement Batch 3 (Chosen)
Implement test data for projects 3506, 3505, 3508, 3507, and 3510. Most are Wokwi-based projects. 3510 is a VGA project.

## 2026-03-14 12:15:00 - Implement Batch 4 of 4 (Projects 3509, 3511, 3514, 3515, 3519)

### Solution 1: Implement Batch 4 (Chosen)
Implement test data for projects 3509, 3511, 3514, 3515, and 3519. This batch contains several VGA projects and a CIC filter.

## 10 Additional TTIHP26a Projects (ID % 5 = 0) (2026-03-16 16:00)

### Solution 1: Targeted Functional Verification (Chosen)
- **Description**: Research and implement specific test cases for each of the 10 selected projects (Gates, VGA, Debounce, Adder, etc.) based on their repository logic.
- **Reasoning**: Ensures each test case is meaningful and accurately reflects the project's unique design and intended behavior.

### Solution 2: Generic Reset and Pattern Test
- **Description**: Use a uniform test template (reset + basic patterns) for all 10 projects regardless of their internal logic.
- **Reasoning for Discarding**: While faster, it fails to verify the specific functionality of complex designs like VGA controllers or debouncers.

### Solution 3: Automated Truth Table Generation
- **Description**: Attempt to automatically generate all possible input combinations for each project.
- **Reasoning for Discarding**: Impractical for sequential designs and results in excessively large YAML files that are difficult to review.
