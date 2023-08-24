from playwright.sync_api import sync_playwright
# 上海悠悠 wx:283340479
# blog:https://www.cnblogs.com/yoyoketang/


with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:12345/')
    # 获取page对象
    page = browser.contexts[0].pages[0]
    print(page.url)
    print(page.title())
    page.get_by_text('新随笔').click()