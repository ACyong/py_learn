class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%r)" % self.data

    def __bool__(self):
        """如果列表中有数据测试位真，则返回True"""
        for x in self.data:
            if x:
                return True
        return False


# L1 = MyList(range(10))
# L1 = MyList([None, False, []])
L1 = MyList([None, False, [None]])
print(L1)
print(bool(L1))

if L1:
    print("L1为真")
else:
    print("L1位假")

L2 = MyList("")
print("L2 = ", L2)




