import re
import urllib.parse
with open('missing_details.txt', 'r') as f:
    content = f.read()
entries = re.findall(r'ID:(\d+)\|NAME:(.*?)\|REPO:(.*?)(?=ID:|\Z)', content, re.DOTALL)
processed = []
for pid, name, repo in entries:
    name = name.strip().replace('\n', ' ')
    repo = repo.strip()
    if 'vga-playground.com' in repo:
        match = re.search(r'repo=(https%3A%2F%2Fgithub\.com%2F.*?)&', repo)
        if match:
            repo = urllib.parse.unquote(match.group(1))
        else:
            match = re.search(r'repo=(https%3A%2F%2Fgithub\.com%2F.*)', repo)
            if match:
                 repo = urllib.parse.unquote(match.group(1))
    processed.append((pid, name, repo))
for pid, name, repo in processed:
    print(f"{pid}|{name}|{repo}")
