import asyncio
import re
import json
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        print("Navigating to shuttle page...")
        await page.goto("https://app.tinytapeout.com/shuttles/ttihp26a")
        try:
            print("Waiting for content to load...")
            await page.wait_for_selector("a[href*='/projects/']", timeout=60000)

            project_links_info = await page.evaluate("""
                () => {
                    const anchors = Array.from(document.querySelectorAll("a"));
                    return anchors.map(a => {
                        const href = a.getAttribute('href') || '';
                        let github = "";
                        if (typeof href === 'string' && href.indexOf('/projects/') !== -1) {
                            // Find the project ID
                            const match = href.match(/\/projects\/(\\d+)/);
                            if (match) {
                                const pid = match[1];
                                // Search the entire document for a GitHub link that might be in the same row/container as this project link
                                // Since we don't know the exact structure, let's look for the row or similar
                                let row = a.closest('tr');
                                if (row) {
                                    const gh = row.querySelector("a[href*='github.com']");
                                    if (gh) github = gh.getAttribute('href') || "";
                                }
                            }
                        }

                        return {
                            href: href,
                            text: a.innerText || a.textContent || "",
                            github: github
                        };
                    });
                }
            """)

            projects = {}
            for info in project_links_info:
                href = info['href']
                if '/projects/' in href:
                    pid_match = re.search(r'/projects/(\d+)', href)
                    if pid_match:
                        pid = pid_match.group(1)
                        name = info['text'].strip()
                        github = info['github']
                        if github and not github.startswith('http'):
                            github = 'https://github.com' + github if github.startswith('/') else 'https://' + github

                        if pid not in projects or (not projects[pid]['repo'] and github):
                            projects[pid] = {'name': name, 'repo': github}

            print(f"FOUND_PROJECTS_START")
            for pid in sorted(projects.keys(), key=int):
                p_data = projects[pid]
                print(f"ID:{pid}|NAME:{p_data['name']}|REPO:{p_data['repo']}")
            print(f"FOUND_PROJECTS_END")

        except Exception as e:
            print(f"Error occurred: {e}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
