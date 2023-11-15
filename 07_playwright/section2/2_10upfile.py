from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("file:///D:/wangyiyun/web_ui/section2/upfile.html")

    page.get_by_label("用户名").fill("yoyo")
    page.get_by_label("文件名称").fill("xx")
    # 文件上传
    # page.get_by_label("选择文件").set_input_files("a1.png")

    # 2.非input文件上传
    # with page.expect_file_chooser() as fc_info:
    #      # page.locator('[name="file"]').click()
    #      page.get_by_label('选择文件').click()
    #
    # file_chooser = fc_info.value
    # file_chooser.set_files('a2.jpg')

    # 3.事件捕获page.on("filechooser") 事件
    page.on("filechooser", lambda file_chooser: file_chooser.set_files("a3.png"))

    # 触发事件
    page.get_by_label('选择文件').click()




    page.pause()
    browser.close()