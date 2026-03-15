import os
import yaml
import re

DATA_DIR = 'src/data'
ROADMAP_FILE = 'ROADMAP.md'
DATE = '2026-03-16'

def get_projects_from_data():
    projects = {}
    for filename in os.listdir(DATA_DIR):
        if filename.endswith('.yaml'):
            id_match = re.search(r'tt(\d+)', filename)
            if id_match:
                pid = id_match.group(1)
                try:
                    with open(os.path.join(DATA_DIR, filename), 'r') as f:
                        data = yaml.safe_load(f)
                        title = data.get('project', 'Unknown')
                        projects[pid] = title
                except:
                    projects[pid] = 'Unknown'
    return projects

def parse_roadmap():
    with open(ROADMAP_FILE, 'rb') as f:
        content = f.read().decode('utf-8', errors='ignore').lstrip('\x00').strip()

    sections = re.split(r'\n## ', content)
    header = sections[0].strip()

    planned_ids = {}
    finished_entries = {}

    for section in sections[1:]:
        lines = section.split('\n')
        title = lines[0].strip()
        body = lines[1:]

        for line in body:
            sline = line.strip()
            if not sline: continue

            if title == 'Planned':
                m = re.search(r'Test-ID: \[(\d+)\]\((.*?)\), Repo: (.*)', sline)
                if m:
                    pid, tt_url, repo = m.groups()
                    planned_ids[pid] = (tt_url, repo)
            elif title == 'Finished':
                m = re.search(r'Test-ID (\d+)', sline)
                if m:
                    pid = m.group(1)
                    if pid not in finished_entries:
                        finished_entries[pid] = sline
                else:
                    if sline not in finished_entries:
                        finished_entries[sline] = sline

    return header, planned_ids, finished_entries

data_projects = get_projects_from_data()
header, planned_ids, finished_entries = parse_roadmap()

# Identify all completed IDs
all_completed = set(finished_entries.keys())
for pid in data_projects:
    all_completed.add(pid)

# Filter planned_ids
remaining_planned = {pid: info for pid, info in planned_ids.items() if pid not in data_projects and pid not in finished_entries}

# Add data projects to finished_entries
for pid, title in data_projects.items():
    if pid not in finished_entries:
        finished_entries[pid] = f"- [x] Create simple testcase for Test-ID {pid} ({title}) ({DATE})"

# Sort IDs descending
sorted_finished_ids = sorted([k for k in finished_entries.keys() if k.isdigit()], key=int, reverse=True)
non_id_finished = [v for k, v in finished_entries.items() if not k.isdigit()]

with open(ROADMAP_FILE, 'w') as f:
    f.write(header + '\n\n')
    f.write('## Planned\n')
    f.write('  - [ ] Create simple testcase for each assigned tile from TTIHP26A shuttle\n')
    for pid in sorted(remaining_planned.keys(), key=int):
        tt_url, repo = remaining_planned[pid]
        f.write(f'    - [ ] Test-ID: [{pid}]({tt_url}), Repo: {repo}\n')
    f.write('  - [ ] Add support for asynchronous signals (Planned)\n')
    f.write('  - [ ] Integrate with GHDL/Verilator for automated verification (Planned)\n')
    f.write('  - [ ] Integration with a simulator to verify test steps (Planned)\n')
    f.write('  - [ ] Improve documentation with examples (Planned)\n')

    f.write('\n## Proposed\n')
    f.write('  - [ ] UI for defining test steps\n')
    f.write('  - [ ] Export to VHDL/Verilog testbench\n')

    f.write('\n## Finished\n')
    for pid in sorted_finished_ids:
        f.write(finished_entries[pid] + '\n')
    for line in non_id_finished:
        f.write(line + '\n')

print("Roadmap updated cleanly with 2/4 indentation.")
