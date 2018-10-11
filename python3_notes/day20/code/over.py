class A:
    def say(self, what):
        print("说", what)

class B(A):
    def say(self, that):
        """此方法覆盖了父类的say方法，它会在B类的对象中优先调用"""
        print("say:", that)

b = B()
b.say("天气好")

A.say(b, "我来调用父类的方法")
B.__base__.say(b, "还是调用父类的方法")
b.__class__.__base__.say(b, "用b来调用父类的方法")


