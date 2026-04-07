import os
template = """project: "{name}"
metadata:
  source: {repo}
signals:
  ui_in: {{name: ui_in, type: input, width: 8}}
  uo_out: {{name: uo_out, type: output, width: 8}}
  uio_in: {{name: uio_in, type: input, width: 8}}
  clk: {{name: clk, type: clock, width: 1}}
  rst_n: {{name: rst_n, type: input, width: 1}}
test_steps:
- name: Reset
  cycles: 1
  values: {{rst_n: 0, ui_in: 0, uio_in: 0}}
- name: Idle
  cycles: 1
  values: {{rst_n: 1, ui_in: 0, uio_in: 0}}
"""
with open('processed_missing.txt', 'r') as f:
    for line in f:
        pid, name, repo = line.strip().split('|')
        safe_name = "".join([c if c.isalnum() else "_" for c in name.lower()]).strip("_")
        safe_name = "_".join(filter(None, safe_name.split("_")))
        filename = f"tt{pid}_{safe_name}.yaml"
        filepath = os.path.join("src/data", filename)
        content = template.format(name=name, repo=repo)
        with open(filepath, 'w') as out:
            out.write(content)
        print(f"Created {filepath}")
