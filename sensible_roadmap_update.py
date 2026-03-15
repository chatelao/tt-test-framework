import os
import yaml
import re

DATA_DIR = 'src/data'
ROADMAP_FILE = 'ROADMAP.md'
DATE = '2026-03-16'

def get_data_projects():
    projects = {}
    for f in os.listdir(DATA_DIR):
        if f.startswith('tt') and f.endswith('.yaml'):
            pid_match = re.search(r'tt(\d+)', f)
            if pid_match:
                pid = pid_match.group(1)
                try:
                    with open(os.path.join(DATA_DIR, f), 'r') as file:
                        data = yaml.safe_load(file)
                        projects[pid] = data.get('project', 'Unknown')
                except:
                    projects[pid] = 'Unknown'
    return projects

def parse_roadmap():
    with open(ROADMAP_FILE, 'r') as f:
        content = f.read()

    sections = re.split(r'\n## ', content)
    header = sections[0].strip()

    planned = []
    proposed = []
    finished = []

    for section in sections[1:]:
        if section.startswith('Planned'):
            planned = section.split('\n')[1:]
        elif section.startswith('Proposed'):
            proposed = section.split('\n')[1:]
        elif section.startswith('Finished'):
            finished = section.split('\n')[1:]

    return header, planned, proposed, finished

data_projects = get_data_projects()
header, planned, proposed, finished = parse_roadmap()

finished_ids = set()
for line in finished:
    m = re.search(r'Test-ID (\d+)', line)
    if m:
        finished_ids.add(m.group(1))

new_finished = []
remaining_planned = []

for line in planned:
    m = re.search(r'Test-ID: \[(\d+)\]', line)
    if m:
        pid = m.group(1)
        if pid in data_projects:
            if pid not in finished_ids:
                title = data_projects[pid]
                new_finished.append(f"- [x] Create simple testcase for Test-ID {pid} ({title}) ({DATE})")
                finished_ids.add(pid)
        else:
            remaining_planned.append(line)
    else:
        # Keep non-ID items in Planned as they are
        remaining_planned.append(line)

# Add remaining data projects not in Roadmap
for pid, title in data_projects.items():
    if pid not in finished_ids:
        new_finished.append(f"- [x] Create simple testcase for Test-ID {pid} ({title}) ({DATE})")
        finished_ids.add(pid)

# Sort new finished descending
new_finished.sort(key=lambda x: int(re.search(r'Test-ID (\d+)', x).group(1)), reverse=True)

with open(ROADMAP_FILE, 'w') as f:
    f.write(header + '\n\n')
    f.write('## Planned\n')
    for line in remaining_planned:
        f.write(line + '\n')

    f.write('\n## Proposed\n')
    for line in proposed:
        f.write(line + '\n')

    f.write('\n## Finished\n')
    # Put new ones at the top of Finished
    for entry in new_finished:
        f.write(entry + '\n')
    for entry in finished:
        f.write(entry + '\n')

print("Roadmap updated minimally.")
