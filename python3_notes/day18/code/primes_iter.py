# primes_iter.py
def prime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5 + 1)):
        if x%i == 0:
            return False
    else:
        return True

class Primes:
    def __init__(self, b, n):
        self.begin = b # 记录起始值
        self.count = n # 记录个数

    def __iter__(self):
        # print("__iter__被调用")
        # 为迭代器添加两个变量
        self.pos = self.begin # pos记录迭代器的当前素数的下一个
        self.yield_count = 0 # 记录已经生成了几个素数
        return self

    def __next__(self):
        """从当前位置开始，判断向后判断哪些时素数，如果遇到素数则返回，
        同时将yield_count做加1操作"""
        if self.yield_count >= self.count:
            raise StopIteration
        while True:
            if prime(self.pos):
                value = self.pos # 得到一个素数
                self.pos += 1 # 把当前位置向后移动
                self.yield_count += 1 # 已产出数加1
                return value
            self.pos += 1



for x in Primes(4, 6):
    print(x)





