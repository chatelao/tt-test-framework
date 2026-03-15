import re

with open('ROADMAP.md', 'r') as f:
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

def get_id(line):
    m = re.search(r'Test-ID (\d+)', line)
    return int(m.group(1)) if m else -1

# Identify new entries (date 2026-03-16)
new_entries = [l for l in finished if '(2026-03-16)' in l]
old_entries = [l for l in finished if '(2026-03-16)' not in l and l.strip()]

new_entries.sort(key=get_id, reverse=True)

with open('ROADMAP.md', 'w') as f:
    f.write(header + '\n\n')
    f.write('## Planned\n')
    for l in planned: f.write(l + '\n')
    f.write('\n## Proposed\n')
    for l in proposed: f.write(l + '\n')
    f.write('\n## Finished\n')
    for l in new_entries: f.write(l.strip() + '\n')
    for l in old_entries: f.write(l.strip() + '\n')
