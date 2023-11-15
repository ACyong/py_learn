from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://47.108.155.10/login.html")

    # 1.定位元素.fill()
    # page.locator('#username').fill("test")
    # page.locator('#password').fill("123456")

    # 2.直接传2个参数
    # page.fill('#username', 'test1')
    # page.fill('#password', '123456')

    # 显示声明css/xpath语法
    # page.locator('css=#username').fill("test")
    # page.locator('xpath=//*[@name="password"]').fill("123456")
    page.fill('css=#username', 'test1')
    page.fill('xpath=//*[@name="password"]', '123456')
    page.pause()

    # text 默认是模糊查找
    # page.locator('text=立即登录').click()
    # 精准匹配
    # page.click("text='立即登录 > '")

    # 组合定位   父元素--->子孙元素   css >> css
    # page.locator('#login-form >> .btn-block').click()
    # 组合  css >> xpath
    # page.locator('#login-form >> //*[@id="loginBtn"]').click()
    # 注意xpath     .//  前面的点不需要
    # css >> text
    # page.locator('#login-form >> text=立即登录').click()
    page.locator("#login-form").locator("text=立即登录").click()




    page.pause()

    browser.close()