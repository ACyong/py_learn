class Dog:
    def __init__(self, k, c="白色"):
        print("__init__被调用")
        self.kinds = k
        self.color = c

    def set_info(self, k, c):
        self.kinds = k
        self.color = c

    def say(self):
        print(self.color, "的", self.kinds, "说：旺！")


dog1 = Dog("京巴")
# dog1.set_info("京巴","白色")
dog1.say()

dog2 = Dog("哈士奇", "灰色")
dog2.say()
