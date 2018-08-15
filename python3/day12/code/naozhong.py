import time

shi = input("设置闹钟提醒时间(00:00:00)：")
L = shi.split(":")
d_h = int(L[0])
d_m = int(L[1])
d_s = int(L[2])

t = time.localtime()
h = t.tm_hour
m = t.tm_min
s = t.tm_sec
while True:
    time.sleep(1)
    if s == 59:
        s = 0
        m += 1
    else:
        s += 1
    if m == 59:
        m = 0
        h += 1
    if h == 23:
        h = 0
    print("\r%02d : %02d : %02d" % (h, m, s), end = "")
    if d_h+d_m+d_s == h+m+s:
        print("\a\a\a\a\a")
        break
print("结束！")
