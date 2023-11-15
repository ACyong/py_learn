from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://v3.bootcss.com/")

    # # 水平 listitem
    # page.get_by_role('listitem').filter(has_text='入门').click()
    # page.pause()

    # dropdown
    dropdown = page.locator('.dropdown')
    dropdown.click()
    # dropdown.get_by_role('listitem').filter(has_text='v5').click()
    dropdown.get_by_role('listitem').filter(has=page.get_by_text('v4')).click()
    page.pause()
