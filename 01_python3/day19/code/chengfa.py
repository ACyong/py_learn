class MyList:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "MyList(%r)" % self.value

    def __mul__(self, rhs):
        return MyList(self.value * rhs)

    def __rmul__(self, lhs):
        """实现反向运算符的重载"""
        return MyList(self.value * lhs)


L1 = MyList([1,2,3])
# L2 = L1 * 3  # L2 = L1.__mul__(3)
# print(L2)

L3 = 3 * L1
# L3 = 3.__mul__(L1)
print(L3)


