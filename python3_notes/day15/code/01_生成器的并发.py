import time


def consumer(name):
    print("%s 准备吃包子！" % name)
    while True:
        baozi = yield
        print("包子[%s] 来了，被[%s] 吃了！" % (baozi, name))


def producer(name):
    c = consumer("A")
    c2 = consumer("B")
    y = c.__next__()
    y1 = c2.__next__()
    print("准备做包子！", y, y1)
    for i in range(10):
        time.sleep(1)
        print("做了2 个包子")
        c.send(i)
        c2.send(i)


producer("庄")
