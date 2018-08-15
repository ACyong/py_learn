import time

def time_monitor(fn):
    def _deco(m):
        begin = time.time() # 获取当前时间
        fn(m)
        end = time.time() # 获取调用后时间
        print("函数myfunc(%d)调用花费了%10.2f秒" % (m, end - begin))
    return _deco
@ time_monitor
def myfun(n):
    s = 0
    for x in range(n):
        s += x
    return s
# 函数执行时间是多少
myfun(100000)
myfun(999999)
myfun(1000000)
print("程序结束！")