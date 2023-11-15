from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("file:///D:/wangyiyun/web_ui/section2/down.html")

    def download_handler(download):
        print(download.suggested_filename)
        download.save_as(download.suggested_filename)

    page.on("download", download_handler)

    page.get_by_text("文件1").click()
    page.get_by_text("文件2").click()
    page.get_by_text("点我下载").click()


    page.wait_for_timeout(60000)
    browser.close()