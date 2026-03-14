import asyncio
from playwright.async_api import async_playwright
import re

async def get_details(pids):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        for pid in pids:
            try:
                url = f"https://app.tinytapeout.com/projects/{pid}"
                await page.goto(url, timeout=30000)
                await page.wait_for_load_state("networkidle")

                # Try to find GitHub link
                repo = ""
                # Look for links that contain github.com but NOT tinytapeout-app
                links = await page.query_selector_all("a[href*='github.com']")
                for link in links:
                    href = await link.get_attribute("href")
                    if "tinytapeout-app" not in href:
                        repo = href
                        break

                # Get name - the one with MuiTypography-h4 seems to be the project title
                name_elem = await page.query_selector("h1.MuiTypography-h4")
                if not name_elem:
                    name_elem = await page.query_selector("h1")

                name = await name_elem.inner_text() if name_elem else "Unknown"
                name = name.strip()

                print(f"ID:{pid}|NAME:{name}|REPO:{repo}")
            except Exception as e:
                print(f"ID:{pid}|ERROR:{e}")
        await browser.close()

if __name__ == "__main__":
    import sys
    pids = sys.argv[1:]
    asyncio.run(get_details(pids))
