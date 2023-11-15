from playwright.sync_api import sync_playwright
"""
query_selector
"""


def handler_alert(dialog):
    print(dialog.message)
    # 自动关闭alert
    dialog.accept()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("file:///C:/Users/dell/Desktop/home.html")

    # 很少用
    frame = page.query_selector('[name="yoyo"]').content_frame()
    print(frame)
    frame.locator('#username').fill('yoyo333')

    page.pause()