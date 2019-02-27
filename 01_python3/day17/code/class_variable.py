class Human:
    home = "地球"  # <---- 此为类变量

    def __init__(self, name):
        self.name = name

    def infos(self):
        print(self.name, '的家园是', self.home)


# print("home = ", home) # 出错，没有这个全局变量
# 获取类的变量
print("Human.home =", Human.home)  # Human.home = 地球

h1 = Human("小张")
h2 = Human("小李")

h1.infos()  # 小张 的家园是 地球
print("h1.home =", h1.home)  # h1.home =  地球
print("h1.home =", h1.__class__.home)  # h1.home =  地球
print("h1.name =", h1.name)  # h1.name = 小张

Human.home = "中国"
h1.infos()  # 小张 的家园是 中国
h2.infos()  # 小李 的家园是 中国

# 类的__doc__属性
#     用于绑定类的文档字符串，当没有文档字符串时，绑定None对象

# 类的__slots__列表
#     __slots__列表
# 作用：限定一个类创建的实例、对象只能有固定的实例变量、属性
























