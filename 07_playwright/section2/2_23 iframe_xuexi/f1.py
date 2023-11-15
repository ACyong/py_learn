from playwright.sync_api import sync_playwright


def dump_frame_tree(frame, indent):
    print(indent + frame.name + '@' + frame.url)
    for child in frame.child_frames:
        dump_frame_tree(child, indent + "    ")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("file:///C:/Users/dell/Desktop/home.html")

    # # 1.定位iframe 元素
    # frame1 = page.frame_locator('[name="yoyo"]')
    # print(frame1)
    # frame1.locator('#username').fill("yoyo")
    # frame1.locator('#password').fill("123456")
    #
    # # 2.frame(name, url)
    # frame2 = page.frame(name="yoyo")
    # print(frame2)
    # frame2.locator('#username').fill("yoyo")
    # frame2.locator('#password').fill("123456")

    # print(page.main_frame)     # 主iframe
    # main = page.main_frame
    # print(main.child_frames)   # 查看所有的子iframe
    # # 查看全部 包含主jframe
    # print(page.frames)

    # for item in page.frames:
    #     print(item.name)   # name 属性    name or id 属性
    #     print(item.url)

    # 遍历页面上 iframe 的层级结构
    # dump_frame_tree(page.main_frame, "")

    # 动态的id的iframe 如何定位
    # css 的正则匹配
    # frame3 = page.frame_locator('[id^="iframe-auto"]')
    # print(frame3)
    # frame3.locator('#username').fill("yoyo")
    # frame3.locator('#password').fill("123456")

    # xpath  contains
    # frame4 = page.frame_locator('//*[contains(@id, "iframe-auto")]')
    # frame4.locator('#username').fill("yoyo")
    # frame4.locator('#password').fill("123456")

    # src 属性
    # frame5 = page.frame_locator('[src="down.html"]')
    # frame5.locator('#username').fill("yoyo")
    # frame5.locator('#password').fill("123456")

    # name url 属性
    # name 属性  id/name  全程
    # frame6 = page.frame(name="yoyo")
    # frame6.locator('#username').fill("yoyo")
    # frame6.locator('#password').fill("123456")

    # frame7 = page.frame(name="yoyo2")
    # frame7.locator('#alert').click()


    # # url 地址 包含部分
    # frame8 = page.frame(url="/login.html")
    # frame8.locator('#username').fill("yoyo")
    # frame8.locator('#password').fill("123456")

    # 2层的iframe
    # frame = page.frame(name="yoyo2").frame_locator('[src="down.html"]')
    # frame.locator('#username').fill("yoyo")
    # frame.locator('#password').fill("123456")



    page.pause()
