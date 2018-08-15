import math


class Square:
    def __init__(self, lside:"边长"):
        self.lside = lside

    def set_side_length(self, v):
        "设置边长"
        self.lside = v

    def get_side_length(self):
        "获取边长"
        return self.lside

    def set_area(self, v):
        "设置面积"
        self.lside = math.sqrt(v)

    def get_area(self):
        "返回面积"
        return self.lside**2

    def __getattr__(self, attrname):
        # print("__getattr__被调用 attrname = ", attrname)
        if attrname == "area":
            return self.lside**2
        raise AttributeError

    def __setattr__(self, attrname, value):
        if attrname == "lside":
            self.__dict__[attrname] = value
        elif attrname == "area":
            self.__dict__['lside'] = value ** 0.5
        else:
            raise AttributeError


s1 = Square(10)
# print(dir(s1))  # dir 函数传入一个对象时，返回对象的实例变量
print("s1的面积是：", s1.area)  # 100
print("s1的边长是：", s1.lside)  # 10
# print(s1.__dict__)
# print(s1.aaaaa)
# print(s1.bbbbb)
# s1.set_area(9)
s1.area = 9
print("s1的面积是：", s1.area)
print("s1的边长是：", s1.lside)
# print(s1.__dict__)
