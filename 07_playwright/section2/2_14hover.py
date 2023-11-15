from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://playwright.dev/", wait_until='domcontentloaded', timeout=60000)

    dropdown = page.locator('.dropdown--hoverable')
    dropdown.hover()

    page.pause()