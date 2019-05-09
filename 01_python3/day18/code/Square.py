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


s1 = Square(10)
print("s1的面积是：", s1.get_area())  # 100
print("s1的边长是：", s1.get_side_length())  # 10
s1.set_area(9)
print("s1的面积是：", s1.get_area())  #
print("s1的边长是：", s1.get_side_length())
