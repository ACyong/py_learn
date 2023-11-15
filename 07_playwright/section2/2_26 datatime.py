"""
日历控件
"""
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('http://124.70.221.221:8200/users/login/')
    page.locator('#username').fill('123@qq.com')
    page.locator('#password_l').fill('123456')
    page.locator('#jsLoginBtn').click()

    page.goto('http://124.70.221.221:8200/users/userinfo/')
    # page.locator('#date_day').clear()
    # page.locator('#date_day').fill('2023-05-07')

    # 去掉readonly 属性
    js1 = 'document.getElementById("birth_day").removeAttribute("readonly");'
    page.evaluate(js1)
    # page.locator('#birth_day').fill('2023-05-06')
    # 直接给输入框赋值
    js2 = 'document.getElementById("birth_day").value="2021-04-01";'
    page.evaluate(js2)


    page.pause()