from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://47.108.155.10/login.html")
    page.get_by_placeholder("请输入用户名").fill("test")
    page.get_by_placeholder("请输入密码").fill("123456")
    page.get_by_role("button", name="立即登录 >").click()

    # 点击新增模块
    page.get_by_text("新增模块").click()
    # form
    page.get_by_label("模块名称:").fill("xxx")

    # 方法1  page.locator().select_option('xx')
    page.get_by_label("所属项目:").select_option("test_xx")
    # 方法2 page.select_option('selector', 'xx')
    page.select_option('#project', 'test_xx')

    page.get_by_label("模块描述:").fill("desc")


    # 打断点
    page.pause()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)