class MyNumber:
    def __init__(self, value):
        self.data = value

    def myadd(self, other):
        return MyNumber(self.data + other.data)

    def __repr__(self):
        return "MyNumber(%d)" % self.data

    def __add__(self, other):
        return MyNumber(self.data + other.data)

    def __sub__(self, other):
        return MyNumber(self.data - other.data)


n1 = MyNumber(100)
n2 = MyNumber(200)
# n3 = n1.myadd(n2)
# n3 = n1.__add__(n2) # 等同于下面一句
# n3 = n1 + n2 # 此时不能这样操作, 没有实现运算符重载，不能进行此类操作
n3 = n1 - n2
print("n3 = ", n3)




int1 = int(100)
int2 = int(200)
int3 = int1 + int2
print("int3 = ", int3)