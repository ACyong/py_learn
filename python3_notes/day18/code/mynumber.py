class MyNumber:
    def __init__(self, value):
        self.data = value

    def __str__(self):
        """转换为给人看的普通字符串"""
        s =  "整数：" + str(self.data)
        return s

    def __repr__(self):
        """转换为给eval能识别的字符串"""
        s = "MyNumber(%d)" % self.data
        return s

    def __abs__(self):
        if self.data < 0:
            return MyNumber(-self.data)
        return MyNumber(self.data)



n1 = MyNumber(100)
n2 = abs(n1)
print(n2)
print("%r" % n1)
print("%s" % n1)
print(repr(n1))
print(str(n1))
