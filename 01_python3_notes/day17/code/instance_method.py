class Dog:
    """这是一种小动物"""
    def say(slef):
        """这是在类内定义的方法
        此方法对于此类的所有对象可以调用self将绑定此方法的实例
        """
        print("旺！")

    def eat(slef, that):
        print("小狗吃：", that)
        slef.food = that

    def food_info(self):
        print("小狗吃上次的是：", self.food)


dog1 = Dog()  # 别忘记加括号
dog1.say()
# Dog.say(dog1)  # 借助于类来直接调用方法（不常用）
dog1.eat("骨头")
dog1.food_info()

dog2 = Dog()
dog2.say()
dog2.eat("狗粮")
dog2.food_info()
