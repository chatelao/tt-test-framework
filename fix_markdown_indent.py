import re

with open('ROADMAP.md', 'r') as f:
    content = f.read()

sections = re.split(r'\n## ', content)
header = sections[0].strip()

def process_section(section_text, is_planned=False):
    lines = section_text.split('\n')
    title = lines[0]
    body = lines[1:]
    new_body = []
    for line in body:
        sline = line.strip()
        if not sline: continue
        if sline.startswith('- ['):
            if is_planned and 'Test-ID:' in sline:
                new_body.append('    ' + sline)
            else:
                new_body.append('  ' + sline)
        else:
            new_body.append(line)
    return title + '\n' + '\n'.join(new_body)

new_sections = [header]
for section in sections[1:]:
    is_planned = section.startswith('Planned')
    new_sections.append(process_section(section, is_planned))

with open('ROADMAP.md', 'w') as f:
    f.write('\n## '.join(new_sections) + '\n')
