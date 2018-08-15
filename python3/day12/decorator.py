"""用装饰器测试一个函数的执行时间"""
import time


def f2(f1):
    def warpper(*args, **kwarge):
        start_time = time.time()
        f1()
        stop_time = time.time()
        print("the f1 run time is %s" % (stop_time - start_time))
    return warpper


@f2
def f1():
    time.sleep(3)
    print("f1 .......")


f1()
