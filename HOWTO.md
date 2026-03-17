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
- `clock`: Clock signal (usually handled automatically by the generator).

## Generating Waveforms

Use the provided script to generate a WaveDrom timing diagram:

```bash
python src/scripts/generate_waveform.py <path_to_yaml>
```

The script will output an `.svg` image in the `waveforms/` directory.
