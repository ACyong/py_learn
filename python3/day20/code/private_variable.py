class A:
    def __init__(self, v):
        self.__money = v

    def get_money(self):
        return self.__money


class B(A):
    """在子类中，无法访问父类的私有变量"""
    def getfathermoney(self):
        # return self._A__money
        return self.__money # 报错

    def __setmoney(self):
        print("这是A类的私有实例方法被调用")

    def test(self):
        self.__setmoney() # 实例方法可以调用自己的私有方法


a = A(10000000)
# print("a的变量__money的值为：", a.__money) # 报错
print("a的变量__money的值为：", a.get_money()) # 报错


b = B(1000)
print(b.getfathermoney())