"""
svg 元素定位
用xpath 语法  //*[name()="svg"] 定位
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("file:///C:/Users/dell/Desktop/svg.html")

    # svg 元素定位
    svg1 = page.locator('//*[@id="box1"]//*[name()="svg"]')
    print(svg1.get_attribute('width'))

    svg2 = page.locator('//*[@id="box2"]//*[name()="svg"]')
    print(svg2.get_attribute('width'))