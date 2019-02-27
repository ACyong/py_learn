import math


class Circle:
    def __init__(self, r):
        self.radius = r

    @property
    def area(self):
        """实现getter方法"""
        return self.radius ** 2 * math.pi

    @area.setter
    def area(self, value):
        """实现setter方法"""
        self.radius = math.sqrt(value / math.pi)

    @property
    def length(self):
        """实现getter方法"""
        return self.radius * 2 * math.pi


c1 = Circle(100)
print("c1的半径是：", c1.radius)
print("c1的面积是：", c1.area)

c1.area = 50
print("c1的半径是：", c1.radius)
print("c1的面积是：", c1.area)
print(c1.__dict__)

c1 = Circle(10)
print("c1的周长是：", c1.length)
