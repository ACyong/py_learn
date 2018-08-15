class Student:
    def __init__(self, n, a, s):

        self.n = n
        self.a = a
        self.s = s

    def infos(self):
        print("我叫:", self.n, "我今年：", self.a, "岁，我的成绩是：", self.s)


class Student2(Student):
    def __init__(self, n, a, s, add='家庭地址不详'):
        super().__init__(n, a, s)
        self.add = add

    def infos(self):
        print("我叫:", self.n, "我今年：", self.a, "岁，我的成绩是：", self.s)
        # 此处需要添加代码
    #     self.add = add
    pass


s1 = Student2("xiao", 20, 100)

s1.infos()