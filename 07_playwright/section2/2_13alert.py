from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("file:///D:/wangyiyun/web_ui/section2/alert.html")


    def handle_dialog(dialog):
        """监听后处理"""
        print(dialog.message)
        print(dialog.type)
        if dialog.type == "prompt":
            print(dialog.default_value)
            dialog.accept(prompt_text='hello world')
        else:
            dialog.dismiss()


    page.on("dialog", handle_dialog)

    page.locator('#alert').click()
    page.locator('#confirm').click()
    page.locator('#prompt').click()



    page.wait_for_timeout(60000)
    browser.close()