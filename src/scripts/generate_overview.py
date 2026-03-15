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

async def get_project_details(pids):
    details = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        for pid in pids:
            try:
                url = f"https://app.tinytapeout.com/projects/{pid}"
                await page.goto(url, timeout=30000)
                # Wait a bit for the SPA to render
                await page.wait_for_timeout(1000)

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

def parse_roadmap():
    projects = []
    with open("ROADMAP.md", "r") as f:
        lines = f.readlines()

    # Matches planned tasks
    # - [ ] Test-ID: [3560](https://app.tinytapeout.com/projects/3560), Repo: ...
    planned_re = re.compile(r"Test-ID: \[(\d+)\]")

    # Matches finished tasks
    # - [x] Create simple testcase for Test-ID 3559 (Just logic) (2026-03-16)
    finished_re = re.compile(r"Test-ID (\d+) \((.*?)\)")

    for line in lines:
        m = planned_re.search(line)
        if m:
            pid = m.group(1)
            projects.append({"id": pid, "name": "Unknown"})
            continue

        m = finished_re.search(line)
        if m:
            pid = m.group(1)
            name = m.group(2)
            # Check if already added
            found = False
            for p in projects:
                if p["id"] == pid:
                    if p["name"] == "Unknown":
                        p["name"] = name
                    found = True
                    break
            if not found:
                projects.append({"id": pid, "name": name})

    return projects

def find_files(pid):
    yaml_file = ""
    svg_file = ""

    for f in os.listdir("src/data"):
        if f.startswith(f"tt{pid}") and f.endswith(".yaml"):
            yaml_file = f"src/data/{f}"
            break

    for f in os.listdir("waveforms"):
        if f.startswith(f"tt{pid}") and f.endswith(".svg"):
            svg_file = f"waveforms/{f}"
            break

    return yaml_file, svg_file

async def main():
    projects_from_roadmap = parse_roadmap()
    # Filter unique IDs
    unique_pids = sorted(list(set(p["id"] for p in projects_from_roadmap)), key=int)

    print(f"Found {len(unique_pids)} projects in ROADMAP.md")

    project_details = await get_project_details(unique_pids)

    with open("TTIHP26A_PROJECTS.md", "w") as f:
        f.write("# TTIHP26A Projects Overview\n\n")
        f.write("| Summary | T-shirt size | Test Data | Waveform | TinyTapeout Page |\n")
        f.write("|---------|--------------|-----------|----------|------------------|\n")

        for pid in unique_pids:
            # Prefer name from scraping, fallback to roadmap
            details = project_details.get(pid, {})
            name = details.get("name", "Unknown")
            if name == "Unknown":
                name = next((p["name"] for p in projects_from_roadmap if p["id"] == pid), "Unknown")

            tiles = details.get("tiles", "Unknown")
            size = get_tshirt_size(tiles)
            yaml_path, svg_path = find_files(pid)

            test_data_link = f"[YAML]({yaml_path})" if yaml_path else "N/A"
            waveform_link = f"[SVG]({svg_path})" if svg_path else "N/A"
            tt_page_link = f"[Project {pid}](https://app.tinytapeout.com/projects/{pid})"

            f.write(f"| {name} | {size} | {test_data_link} | {waveform_link} | {tt_page_link} |\n")

    print("Generated TTIHP26A_PROJECTS.md")

if __name__ == "__main__":
    asyncio.run(main())
