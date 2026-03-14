# TT Test Framework

A YAML-based test framework to define and verify test steps for Tiny-Tapeout projects.

## Overview

This tool allows you to define the operational sequence of your Tiny-Tapeout project in a structured YAML format. It can then generate PlantUML timing diagrams to visualize the protocol.

## Features

- **YAML-based**: Easy to read and maintain test sequences.
- **Waveform Generation**: Automatically creates PlantUML timing diagrams.
- **MicroPython Compatible**: Designed to reflect steps used in hardware testing with the TT DevKit.

## Project Structure

- `src/schema`: Defines the YAML structure.
- `src/data`: Contains test cases (e.g., MicroPython example).
- `src/scripts`: Tooling for waveform generation.
- `src/puml`: Generated PlantUML source files.
- `images`: Generated PNG waveforms.
- `test`: End-to-end tests for the framework.

## Quick Start

1. Define your test steps in `src/data/my_test.yaml`.
2. Run the generator:
   ```bash
   python src/scripts/generate_waveform.py src/data/my_test.yaml
   ```
3. View the resulting `.puml` file in `src/puml/` and `.png` in `images/`.
