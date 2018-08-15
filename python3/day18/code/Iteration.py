"""类 MyIter"""
class MyInteger:
    """MyIteger类是一个能够生成一系列整数的类
    他的实例对象是可迭代对象"""
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        """此方法返回一个迭代器，
        此迭代器必须能用next取值
        有__iter__函数的对象为可迭代对象"""
        print("__iter__被调用")
        self.iter_pos = self.start # 每次调用iter时，初始化位置
        return self

    def __next__(self):
        """这里实现迭代器协议"""
        print("__next__被调用")
        if self.iter_pos >= self.stop:
            raise StopIteration
        # 还有数据
        value = self.iter_pos
        self.iter_pos += 1 # 迭代位置向后移动一个位置
        return value # 返回当前的值


# obj = MyInteger(3, 6)
# it = iter(obj)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# for x in MyInteger(3, 6):
#     print(x)
it = iter(MyInteger(3, 6))
try:
    while True:
        x = next(it)
        print(x)
except StopIteration:
    raise StopIteration


















