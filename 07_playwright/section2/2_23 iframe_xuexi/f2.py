from playwright.sync_api import sync_playwright
"""
page.on()  可以监听主页面以及 iframe 上的事件
"""


def handler_alert(dialog):
    print(dialog.message)
    # 自动关闭alert
    dialog.accept()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("file:///C:/Users/dell/Desktop/home.html")

    # 事件监听
    # page.on('dialog', handler_alert)
    #
    # frame7 = page.frame(name="yoyo2")
    # frame7.locator('#alert').click()


    # 执行 javascript
    frame = page.frame(name="yoyo")
    js = "document.getElementById('username').value='yoyo234'"
    frame.evaluate(js)

    # page.evaluate('alert("hello world")')





    page.pause()
