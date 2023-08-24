from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://47.108.155.10/login.html")
    page.get_by_placeholder("请输入用户名").click()
    page.get_by_placeholder("请输入用户名").fill("test")
    page.get_by_placeholder("请输入密码").click()
    page.get_by_placeholder("请输入密码").fill("123456")

    # 断点
    page.pause()

    page.get_by_role("button", name="立即登录 >").click()

    # 打断点
    # page.pause()1

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)