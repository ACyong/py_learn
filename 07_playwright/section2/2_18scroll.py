from playwright.sync_api import sync_playwright


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False, slow_mo=2000)
    page = browser.new_page()

    page.goto("https://www.runoob.com/")
    # click 自动滚动到元素出现的位置
    # page.get_by_text('【学习 Django】').click()


    # 滚动到元素出现的位置
    # page.get_by_text('【学习 Django】').scroll_into_view_if_needed()

    page.get_by_text('【学习 Django】').hover()
    page.pause()
