from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("file:///D:/wangyiyun/web_ui/section2/down.html")

    with page.expect_download() as download_info:
        page.get_by_text("点我下载").click()
    download = download_info.value
    # 保存下载
    path = download.path()
    print(path)   # 下载文件的路径
    print(download.url)
    # 保存到本地
    download.save_as(download.suggested_filename)


    browser.close()
