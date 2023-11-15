"""
action:
fill

延迟
slow_mo  每个动作 action 间隔时间
type 输入延迟 delay=2000
"""

from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    page = browser.new_page()
    page.goto("http://47.108.155.10/login.html")
    # text 文本选择器
    # page.locator('#username').fill("test")
    # page.get_by_label('用 户 名:').fill('test')
    # page.fill('#username', 'test')
    # page.locator('#username').type('hello world', delay=2000)

    page.pause()
    browser.close()