"""
单选框和复选框相关操作总结
locator.click()  点击操作
locator.check()   选中
locator.uncheck()  不选中
locator.set_checked()  设置选中状态
locator.is_checked()  判断是否被选中
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("file:///D:/wangyiyun/web_ui/section2/checkbox.html")

    # radio 1. click
    # page.locator('#woman').click()
    # print(page.locator('#woman').is_checked())

    # 2.check()
    # page.locator('#woman').check()
    # print(page.locator('#woman').is_checked())

    # 3..set_checked(checked=True)
    # page.locator('#woman').set_checked(checked=True)
    # print(page.locator('#woman').is_checked())

    # radio 不能设置 uncheck
    # page.locator('#man').uncheck()

    # checkbox  click
    page.locator('#a1').click()
    print(page.locator('#a1').is_checked())

    page.locator('#a3').click()
    print(page.locator('#a3').is_checked())

    # 需求---某个必须选中
    page.locator('#a3').check()     # 必须选中
    print(page.locator('#a3').is_checked())


    page.locator('#a3').uncheck()   # 必须不选中
    print(page.locator('#a3').is_checked())


    # 设置是否选中 set_checked(checked=True)

    page.locator('#a4').set_checked(checked=True)

    page.locator('#a4').set_checked(checked=False)


    # 设置全部为选中
    box = page.locator('[type="checkbox"]').all()    # 获取全部元素
    for item in box:
        item.check()
    page.pause()




