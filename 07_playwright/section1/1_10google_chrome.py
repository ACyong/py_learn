from playwright.sync_api import sync_playwright
import getpass
print(getpass.getuser())

USER_DIR_PATH = f"C:\\Users\\{getpass.getuser()}\\AppData\Local\Google\Chrome\\User Data"


with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir=USER_DIR_PATH,
        # 接收下载事件
        accept_downloads=True,
        channel='chrome',
        bypass_csp=True,
        headless=False
    )
    page = context.new_page()
    page.goto("https://www.cnblogs.com/yoyoketang/")
    print(page.title())
    page.pause()

    context.close()