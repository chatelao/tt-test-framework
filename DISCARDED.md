# Discarded Solutions

## YAML Schema for Test Steps

### Solution 1: Cycle-based (2025-05-22 10:00)
- **Description**: A list where each entry represents a single clock cycle and defines the state of all pins.
- **Reason for Discarding**: Too verbose and repetitive for long sequences like the 32-element stream.

### Solution 2: Pin-grouped (2025-05-22 10:05)
- **Description**: A dictionary where each key is a pin name, and the value is a list of time-value pairs.
- **Reason for Discarding**: Makes it difficult to see the synchronized state of all pins at a specific cycle, which is important for protocol debugging.

## Waveform Generation

### Solution 1: Local PlantUML Jar (2025-05-22 10:10)
- **Description**: Download and run the PlantUML Java executable locally.
- **Reason for Discarding**: Requires Java runtime and might have environment dependencies that are not guaranteed in the sandbox.

### Solution 2: Manual SVG Generation (2025-05-22 10:15)
- **Description**: Write a custom script to generate SVG directly from YAML.
- **Reason for Discarding**: High complexity and redundant given PlantUML's existing capabilities for timing diagrams.
