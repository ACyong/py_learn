from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("http://47.108.155.10/login.html")
    page.get_by_placeholder("请输入用户名").click()
    page.get_by_placeholder("请输入用户名").fill("test")
    page.get_by_placeholder("请输入密码").click()
    page.get_by_placeholder("请输入密码").fill("123456")
    page.get_by_role("button", name="立即登录 >").click()