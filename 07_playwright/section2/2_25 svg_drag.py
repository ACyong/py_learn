"""
svg 元素拖动
page.mouse 鼠标事件
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("file:///C:/Users/dell/Desktop/drag/snap_events.html")

    circle = page.locator('//*[name()="svg"]/*[name()="circle"]')
    # 元素添加事件监听
    circle.evaluate('node => node.addEventListener("mousedown", function(){console.log("目标元素被鼠标down了");});')

    # 获取坐标
    print(circle.bounding_box())
    box = circle.bounding_box()
    # 按住元素正中心的位置
    page.mouse.move(x=box['x']+box['width']/2, y=box['y']+box['height']/2)
    page.mouse.down()
    page.mouse.move(x=box['x']+box['width']/2+100, y=box['y']+box['height']/2)
    page.mouse.up()
    page.pause()

