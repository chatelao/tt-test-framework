# TT Test Framework

A YAML-based test framework to define and verify test steps for Tiny-Tapeout projects.

## Overview

This tool allows you to define the operational sequence of your Tiny-Tapeout project in a structured YAML format. It can then generate WaveDrom timing diagrams to visualize the protocol.

## Features

- **YAML-based**: Easy to read and maintain test sequences.
- **Waveform Generation**: Automatically creates WaveDrom timing diagrams.
- **MicroPython Compatible**: Designed to reflect steps used in hardware testing with the TT DevKit.

## Documentation

The full documentation is available at [tt-test-framework.readthedocs.io](https://tt-test-framework.readthedocs.io/).

## Project Structure

- `src/schema`: Defines the YAML structure.
- `src/data`: Contains test cases (e.g., MicroPython example).
- `src/scripts`: Tooling for waveform generation and documentation.
- `src/docs`: Generated documentation for each test set.
- `waveforms`: Generated SVG waveforms.
- `test`: End-to-end tests for the framework.

## Quick Start

1. Define your test steps in `src/data/my_test.yaml`.
2. Run the generator:
   ```bash
   python src/scripts/generate_waveform.py src/data/my_test.yaml
   ```
3. View the resulting `.svg` in `waveforms/`.
