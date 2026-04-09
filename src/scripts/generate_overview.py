import asyncio
import re
import os
from playwright.async_api import async_playwright

def get_tshirt_size(tiles):
    if not tiles or tiles == "Unknown":
        return "Unknown"

    mapping = {
        "1x1": "S",
        "1x2": "M",
        "2x2": "L",
        "4x2": "XL",
        "8x2": "XXL",
        "4x4": "XXL",
        "8x4": "XXXL"
    }
    if tiles in mapping:
        return mapping[tiles]

    # Try to calculate based on number of tiles if not in mapping
    try:
        w, h = map(int, tiles.split('x'))
        total = w * h
        if total <= 1: return "S"
        if total <= 2: return "M"
        if total <= 4: return "L"
        if total <= 8: return "XL"
        if total <= 16: return "XXL"
        return "XXXL"
    except:
        return tiles

def get_novelty_stars(size):
    mapping = {
        "S": "⭐",
        "M": "⭐⭐",
        "L": "⭐⭐⭐",
        "XL": "⭐⭐⭐⭐",
        "XXL": "⭐⭐⭐⭐⭐",
        "XXXL": "⭐⭐⭐⭐⭐"
    }
    return mapping.get(size, "N/A")

async def get_project_details(pids):
    details = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        for pid in pids:
            try:
                url = f"https://app.tinytapeout.com/projects/{pid}"
                await page.goto(url, timeout=30000)
                # Wait for the specific title element if possible, or network idle
                try:
                    await page.wait_for_selector("h1.MuiTypography-h4", timeout=5000)
                except:
                    await page.wait_for_load_state("networkidle")

                # Extract Tiles
                tiles = "Unknown"
                # Look for a div or span that contains "Tiles:" and then the size
                body_text = await page.inner_text("body")
                tile_match = re.search(r"Tiles:\s*(\d+x\d+)", body_text)
                if tile_match:
                    tiles = tile_match.group(1)

                # Extract Name
                name = "Unknown"
                name_elem = await page.query_selector("h1.MuiTypography-h4")
                if not name_elem:
                    name_elem = await page.query_selector("h1")
                if name_elem:
                    name = await name_elem.inner_text()
                    name = name.strip().split('\n')[0] # Only take first line

                details[pid] = {"tiles": tiles, "name": name}
                print(f"Fetched ID:{pid}, Name:{name}, Tiles:{tiles}")
            except Exception as e:
                print(f"Error fetching ID:{pid}: {e}")
                details[pid] = {"tiles": "Unknown", "name": "Unknown"}
        await browser.close()
    return details

def get_title_from_yaml(yaml_path):
    if not yaml_path or not os.path.exists(yaml_path):
        return None
    try:
        with open(yaml_path, 'r') as f:
            content = f.read()
            m = re.search(r'project:\s*(.*)', content)
            if m:
                return m.group(1).strip()
    except:
        pass
    return None

def parse_roadmap():
    roadmap_data = {} # pid -> {"name": ..., "reason": ...}
    if not os.path.exists("ROADMAP.md"):
        return roadmap_data

    with open("ROADMAP.md", "r") as f:
        lines = f.readlines()

    planned_re = re.compile(r"Test-ID: \[(\d+)\]")
    finished_re = re.compile(r"Test-ID (\d+) \((.*?)\)")
    skip_re = re.compile(r"\(Skipped - (.*?)\)")

    for line in lines:
        pid = None
        name = "Unknown"
        reason = None

        m_skip = skip_re.search(line)
        if m_skip:
            reason = m_skip.group(1)

        m_planned = planned_re.search(line)
        if m_planned:
            pid = m_planned.group(1)
        else:
            m_finished = finished_re.search(line)
            if m_finished:
                pid = m_finished.group(1)
                name = m_finished.group(2)

        if pid:
            if pid not in roadmap_data:
                roadmap_data[pid] = {"name": name, "reason": reason}
            else:
                if roadmap_data[pid]["name"] == "Unknown" and name != "Unknown":
                    roadmap_data[pid]["name"] = name
                if roadmap_data[pid]["reason"] is None and reason is not None:
                    roadmap_data[pid]["reason"] = reason

    # Also check if it is skipped based on titles like " (Skipped - Analog)"
    for pid in roadmap_data:
        name = roadmap_data[pid]["name"]
        if " (Skipped - " in name:
            s_match = re.search(r" \(Skipped - (.*?)\)", name)
            if s_match:
                roadmap_data[pid]["reason"] = s_match.group(1)
                roadmap_data[pid]["name"] = name.replace(s_match.group(0), "")

    return roadmap_data

def find_files(pid):
    yaml_path = ""
    svg_path = ""

    if os.path.exists("src/data"):
        for f in os.listdir("src/data"):
            if f.startswith(f"tt{pid}") and f.endswith(".yaml"):
                yaml_path = f"src/data/{f}"
                break

    if os.path.exists("waveforms"):
        # First priority: SVG matching the YAML filename (minus extension)
        if yaml_path:
            yaml_name = os.path.splitext(os.path.basename(yaml_path))[0]
            target_svg = f"waveforms/{yaml_name}.svg"
            if os.path.exists(target_svg):
                svg_path = target_svg

        # Second priority: Any SVG starting with tt{pid}
        if not svg_path:
            for f in os.listdir("waveforms"):
                if f.startswith(f"tt{pid}") and f.endswith(".svg"):
                    svg_path = f"waveforms/{f}"
                    break

    return yaml_path, svg_path

async def main():
    # Collect all PIDs
    all_pids = set()

    # From Roadmap
    roadmap_data = parse_roadmap()
    all_pids.update(roadmap_data.keys())

    # From Files
    if os.path.exists("src/data"):
        for f in os.listdir("src/data"):
            m = re.search(r"tt(\d+)", f)
            if m: all_pids.add(m.group(1))

    if os.path.exists("waveforms"):
        for f in os.listdir("waveforms"):
            m = re.search(r"tt(\d+)", f)
            if m: all_pids.add(m.group(1))

    # Remove obvious non-IDs (like 26 from ttihp26a if accidentally caught)
    # tt IDs are usually 4 digits in this shuttle (starting 3390)
    unique_pids = sorted([p for p in all_pids if len(p) >= 4], key=int)

    print(f"Total projects identified: {len(unique_pids)}")

    project_details = await get_project_details(unique_pids)

    testable_projects = []
    untestable_projects = []

    for pid in unique_pids:
        yaml_path, svg_path = find_files(pid)
        yaml_title = get_title_from_yaml(yaml_path)

        details = project_details.get(pid, {})
        fetched_name = details.get("name", "Unknown")
        roadmap_name = roadmap_data.get(pid, {}).get("name", "Unknown")

        # Priority: YAML > Roadmap > Fetched > Unknown
        name = yaml_title
        if not name or name == "Unknown" or name == "Tiny Tapeout":
            if roadmap_name != "Unknown":
                name = roadmap_name
            else:
                name = fetched_name

        # Clean up quotes if present
        if name.startswith('"') and name.endswith('"'):
            name = name[1:-1]

        tiles = details.get("tiles", "Unknown")
        size = get_tshirt_size(tiles)
        novelty = get_novelty_stars(size)
        yaml_path, svg_path = find_files(pid)

        reason = roadmap_data.get(pid, {}).get("reason")

        project_info = {
            "id": pid,
            "name": name,
            "novelty": novelty,
            "size": size,
            "yaml_path": yaml_path,
            "svg_path": svg_path,
            "reason": reason
        }

        if reason:
            untestable_projects.append(project_info)
        else:
            testable_projects.append(project_info)

    # Sort by complexity (T-shirt size) descending, then by ID ascending
    complexity_map = {"S": 1, "M": 2, "L": 3, "XL": 4, "XXL": 5, "XXXL": 6, "Unknown": 0}
    testable_projects.sort(key=lambda x: (-complexity_map.get(x["size"], 0), int(x["id"])))
    untestable_projects.sort(key=lambda x: (-complexity_map.get(x["size"], 0), int(x["id"])))

    with open("src/docs/TTIHP26A_PROJECTS.md", "w") as f:
        f.write("# TTIHP26A Projects Overview\n\n")

        f.write("## Testable Designs\n\n")
        f.write("| Summary | Novelty | T-shirt size | Test Data | Waveform | TinyTapeout Page |\n")
        f.write("|---------|---------|--------------|-----------|----------|------------------|\n")
        for p in testable_projects:
            # Check if a markdown file exists
            md_path = f"src/docs/tt{p['id']}.md"
            if os.path.exists(md_path):
                name_link = f"[{p['name']}](tt{p['id']}.md)"
            else:
                name_link = f"[{p['name']}](tt{p['id']}.md)"
            yaml_rel = p['yaml_path'].replace("src/data/", "data/") if p['yaml_path'] else ""
            svg_rel = p['svg_path'].replace("waveforms/", "waveforms/") if p['svg_path'] else ""

            test_data_link = f"[YAML]({yaml_rel})" if yaml_rel else "N/A"
            waveform_link = f"[SVG]({svg_rel})" if svg_rel else "N/A"
            tt_page_link = f"[Project {p['id']}](https://app.tinytapeout.com/projects/{p['id']})"
            f.write(f"| {name_link} | {p['novelty']} | {p['size']} | {test_data_link} | {waveform_link} | {tt_page_link} |\n")

        f.write("\n## Untestable Designs\n\n")
        f.write("| Summary | Novelty | T-shirt size | Why | TinyTapeout Page |\n")
        f.write("|---------|---------|--------------|-----|------------------|\n")
        for p in untestable_projects:
            # Check if a markdown file exists even for untestable projects
            md_path = f"src/docs/tt{p['id']}.md"
            if os.path.exists(md_path):
                name_link = f"[{p['name']}](tt{p['id']}.md)"
            else:
                name_link = f"[{p['name']}](tt{p['id']}.md)"
            tt_page_link = f"[Project {p['id']}](https://app.tinytapeout.com/projects/{p['id']})"
            f.write(f"| {name_link} | {p['novelty']} | {p['size']} | {p['reason']} | {tt_page_link} |\n")

    print("Generated TTIHP26A_PROJECTS.md")

if __name__ == "__main__":
    asyncio.run(main())
