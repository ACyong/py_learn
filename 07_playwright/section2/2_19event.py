from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("file:///D:/wangyiyun/web_ui/section2/alert.html")

    def dialog_handler(dialog):
        print(dialog.message)
        dialog.dismiss()

    # page.on('dialog', dialog_handler)
    #
    #
    # page.pause()
    # 取消监听
    # page.remove_listener('dialog', dialog_handler)
    # page.pause()


    # 只监听一次
    page.once('dialog', dialog_handler)
    page.pause()
