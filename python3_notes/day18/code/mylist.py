class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%r)" % self.data

    def __int__(self):
        """对于int(obj)函数调用时回调用到此方法
        调用此方法时，返回容器内所有元素的和
        """
        return sum(self.data)

L1 = MyList(range(10))
print(L1)
int1 = int(L1)
print(int1)

