class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def hot_potato(namelist, num):
    """
    弗拉维奥·约瑟夫斯是 公元 1 世纪著名的历史学家。
    相传，约瑟夫斯当年和 39 个战友在山洞中对抗罗马军队。
    眼看着即将失败，他们决定舍生取义。
    于是，他们围成一圈，从某个人开始，按顺时针方向杀掉第 7 人
    """
    sim_queue = Queue()
    for name in namelist:
        sim_queue.enqueue(name)
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
