# Usage Instructions

## Defining Test Steps

Create a YAML file in `src/data/`. The file should follow this structure:

```yaml
project: "Project Name"
signals:
  SIGNAL_NAME:
    type: "input"
    width: 8
test_steps:
  - name: "Phase 1"
    cycles: 1
    values:
      SIGNAL_NAME: 0xFF
```

### Signal Types
- `input`: Signals driven into the chip.
- `output`: Signals coming from the chip.
- `clock`: Clock signal. If a signal is defined with this type, it will be used as the reference clock in the waveform instead of the default `CLK`.

## Advanced Metadata

The `metadata` section at the root of the YAML file supports additional flags:

- `async`: (boolean) If set to `true`, no automatic clock signal (default `CLK` or custom `clock` types) will be rendered in the timing diagram. This is useful for pure combinational designs.

Example:
```yaml
project: "Combinational Logic"
metadata:
  async: true
signals:
  ui_in: {type: "input", width: 8}
  uo_out: {type: "output", width: 8}
test_steps:
  - name: "Step 1"
    cycles: 1
    values: {ui_in: 0x55}
```

## Generating Waveforms

Use the provided script to generate a WaveDrom timing diagram:

```bash
python src/scripts/generate_waveform.py <path_to_yaml>
```

The script will output an `.svg` image in the `waveforms/` directory.
