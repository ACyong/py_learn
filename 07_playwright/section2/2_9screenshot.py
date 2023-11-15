from playwright.sync_api import sync_playwright
import base64


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    page = browser.new_page()
    # page.goto("https://www.cnblogs.com/yoyoketang/")
    #
    # # 1.截图当前窗口
    # page.screenshot(path='a1.png')
    # page.screenshot(path='a2.jpg')
    # # 2.截取全屏长图
    # page.screenshot(path='a3.png', full_page=True)
    #
    # # 3.对某个元素截图
    page.goto("https://www.baidu.com")
    # page.locator('#form').screenshot(path='x.png')
    # 4.捕获数据流
    screenshot_bytes = page.locator('#form').screenshot()
    print(screenshot_bytes)
    print(base64.b64encode(screenshot_bytes).decode())


    page.pause()
    browser.close()