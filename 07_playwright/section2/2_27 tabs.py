"""
多标签页窗口切换
"""
from playwright.sync_api import sync_playwright
# 上海悠悠 wx:283340479
# blog:https://www.cnblogs.com/yoyoketang/


def switch_to_page(context, title=None, url=None):
    """切换到指定title 名称 或 url 的 标签页"""
    for item_page in context.pages:
        if title:
            if title in item_page.title():
                # 激活当前选项卡
                item_page.bring_to_front()
                return item_page
        elif url:
            if url in item_page.url:
                # 激活当前选项卡
                item_page.bring_to_front()   # 视觉切换，功能不影响
                return item_page
    else:
        print("not found title or url")
    return context.pages[0]


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.baidu.com')

    # 点开多个标签页
    for link in page.locator('#s-top-left>a').all():
        link.click()

    print(page.title())

    # 获取所有的page对象
    print(context.pages)
    # for p in context.pages:
    #     if "百度地图" in p.title():
    #         print(p.url)
    #         print(p.title())

    new_page = switch_to_page(context, title="地图")
    print(new_page.url)


    page.pause()
