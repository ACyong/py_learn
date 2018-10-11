# import time
# def clock():
#     while True:
#         t = time.localtime()
#         h, m, s = t[3:6]
#         print("%02d : %02d : %02d" % (h, m, s), end = "\r")
#         time.sleep(1)

# clock()

import time


def clock():
    while True:
        t = time.localtime()
        h, m, s = t[3:6]
        print("%02d : %02d : %02d" % (h, m, s), end="\r")
        if hour == h and minute == m:
            print("时间到！！")
            break
        time.sleep(1)


hour = int(input("请输入小时："))
minute = int(input("请输入分钟："))

clock()
