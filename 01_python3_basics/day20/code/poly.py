class Shape:
    def draw(self):
        pass

class Point(Shape):
    def draw(self):
        print("正在画一个点")

class Circle(Point):
    def draw(self):
        print("正在画一个圆")


def my_draw(obj):
    obj.draw() # 动态调用相应的方法（动态）

L = [Point(), Circle()]
for x in L:
    my_draw(x)