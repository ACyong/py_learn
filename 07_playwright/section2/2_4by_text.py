"""
内置定位方法
- page.get_by_text() 通过文本内容定位。
- page.get_by_label() 通过关联标签的文本定位表单控件。
- page.get_by_placeholder() 按占位符定位输入。
- page.get_by_title() 通过标题属性定位元素。
- page.get_by_role() 通过显式和隐式可访问性属性进行定位。
- page.get_by_alt_text() 通过替代文本定位元素，通常是图像。
- page.get_by_test_id() 根据 data-testid 属性定位元素（可以配置其他属性）
"""

from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://47.108.155.10/login.html")
    # text 文本选择器
    print(page.title())
    page.get_by_text("没有账号？点这注册").click()

    print(page.title())
    # 断言页面上的文本是可见的
    # t = page.get_by_text("注册账号")

    # 完全匹配文本
    # // * [text() = "上海悠悠"]
    # 包含某个文本
    #  // * [contains(text(), "上海悠悠")]

    x = page.locator('//*[text()="注册账号"]')
    expect(x).to_be_visible()   # 可见
    page.query_selector()

    page.pause()
    browser.close()

