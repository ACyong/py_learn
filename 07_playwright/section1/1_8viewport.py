from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    # args=['--start-maximized']
    browser = p.chromium.launch(headless=False, args=['--start-maximized'])
    # context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = browser.new_page(no_viewport=True)
    page.goto("https://www.baidu.com")
    print(page.title())
    page.pause()

    browser.close()
