import sys
from ruamel.yaml import YAML
import os

yaml = YAML()
yaml.preserve_quotes = True

def update_tt3990():
    filepath = 'src/data/tt3990_fp8_mul.yaml'
    with open(filepath, 'r') as f:
        data = yaml.load(f)

    bitfields = [
        {
            "name": "Cycle 0: Metadata Load",
            "items": [
                {
                    "signal": "ui_in",
                    "description": "Metadata 0",
                    "svg": "tt3990_ui_in_c0",
                    "reg": {"reg": [{"name": "NBM Offset A", "bits": 3}, {"name": "LNS Mode", "bits": 2}, {"name": "Loopback", "bits": 1}, {"name": "Debug", "bits": 1}, {"name": "Short Protocol", "bits": 1}], "config": {"hspace": 800}}
                },
                {
                    "signal": "uio_in",
                    "description": "Metadata 1",
                    "svg": "tt3990_uio_in_c0",
                    "reg": {"reg": [{"name": "NBM Offset B", "bits": 3}, {"name": "Rounding Mode", "bits": 2}, {"name": "Overflow", "bits": 1}, {"name": "Packed Mode", "bits": 1}, {"name": "MX+ Enable", "bits": 1}], "config": {"hspace": 800}}
                }
            ]
        },
        {
            "name": "Cycle 1: Scale A & Config A",
            "items": [
                {
                    "signal": "ui_in",
                    "description": "Scale A (8-bit Unsigned)",
                    "svg": "tt3990_data_8b",
                    "reg": {"reg": [{"name": "Scale", "bits": 8}], "config": {"hspace": 800}}
                },
                {
                    "signal": "uio_in",
                    "description": "Config A",
                    "svg": "tt3990_uio_in_c1",
                    "reg": {"reg": [{"name": "Format", "bits": 3}, {"name": "BM Index", "bits": 5}], "config": {"hspace": 800}}
                }
            ]
        },
        {
            "name": "Cycle 2: Scale B & Config B",
            "items": [
                {
                    "signal": "ui_in",
                    "description": "Scale B (8-bit Unsigned)",
                    "svg": "tt3990_data_8b",
                    "reg": {"reg": [{"name": "Scale", "bits": 8}], "config": {"hspace": 800}}
                },
                {
                    "signal": "uio_in",
                    "description": "Config B",
                    "svg": "tt3990_uio_in_c2",
                    "reg": {"reg": [{"name": "Format", "bits": 3}, {"name": "BM Index", "bits": 5}], "config": {"hspace": 800}}
                }
            ]
        },
        {
            "name": "Cycles 3-34: Element Streaming",
            "items": [
                {
                    "signal": "ui_in",
                    "description": "Element A_i (8-bit Float/Int)",
                    "svg": "tt3990_data_8b",
                    "reg": {"reg": [{"name": "Data", "bits": 8}], "config": {"hspace": 800}}
                },
                {
                    "signal": "uio_in",
                    "description": "Element B_i (8-bit Float/Int)",
                    "svg": "tt3990_data_8b",
                    "reg": {"reg": [{"name": "Data", "bits": 8}], "config": {"hspace": 800}}
                }
            ]
        },
        {
            "name": "Cycles 37-40: Result Output",
            "items": [
                {
                    "signal": "uo_out",
                    "description": "Result Byte (serialized MSB to LSB)",
                    "svg": "tt3990_data_8b",
                    "reg": {"reg": [{"name": "Result", "bits": 8}], "config": {"hspace": 800}}
                }
            ]
        }
    ]
    data['bitfields'] = bitfields
    with open(filepath, 'w') as f:
        yaml.dump(data, f)

def update_tt3415():
    filepath = 'src/data/tt3415_simproc.yaml'
    with open(filepath, 'r') as f:
        data = yaml.load(f)

    bitfields = [
        {
            "name": "Config BAUD",
            "items": [
                {
                    "signal": "uio_in",
                    "description": "BAUD Rate (Cycles per bit = {uio_in, 2'b00})",
                    "svg": "tt3415_uio_in_baud",
                    "reg": {"reg": [{"name": "BAUD[7:0]", "bits": 8}], "config": {"hspace": 800}}
                }
            ]
        }
    ]
    data['bitfields'] = bitfields
    with open(filepath, 'w') as f:
        yaml.dump(data, f)

def update_tt3641():
    filepath = 'src/data/tt3641_m31_accel.yaml'
    with open(filepath, 'r') as f:
        data = yaml.load(f)

    bitfields = [
        {
            "name": "Control Mapping (uio_in)",
            "items": [
                {
                    "signal": "uio_in",
                    "description": "Command and Register Selection",
                    "svg": "tt3641_uio_in_ctrl",
                    "reg": {"reg": [{"name": "CMD_EN", "bits": 1}, {"name": "REG_SEL[0]", "bits": 1}, {"name": "RW", "bits": 1}, {"name": "REG_SEL[1]", "bits": 1}, {"bits": 4, "name": "unused"}], "config": {"hspace": 800}}
                }
            ]
        }
    ]
    data['bitfields'] = bitfields
    with open(filepath, 'w') as f:
        yaml.dump(data, f)

def update_tt3991():
    filepath = 'src/data/tt3991_processor2.yaml'
    with open(filepath, 'r') as f:
        data = yaml.load(f)

    bitfields = [
        {
            "name": "Load Mode Control (uio_in)",
            "items": [
                {
                    "signal": "uio_in",
                    "description": "Programming Protocol Control",
                    "svg": "tt3991_uio_in_load",
                    "reg": {"reg": [{"name": "LOAD_MODE", "bits": 1}, {"name": "LOAD_VALID", "bits": 1}, {"bits": 6, "name": "unused"}], "config": {"hspace": 800}}
                }
            ]
        }
    ]
    data['bitfields'] = bitfields
    with open(filepath, 'w') as f:
        yaml.dump(data, f)

if __name__ == "__main__":
    update_tt3990()
    update_tt3415()
    update_tt3641()
    update_tt3991()
    print("Updated YAMLs with bitfield metadata.")
