class A:
    def hello(self):
        print("A类里面的hello被调用！")

class B(A):
    def hello(self):
        print("B类里面的hello被调用！")

    def say(self):
        self.hello()
        super(B, self).hello() # 调用A类的hello方法
        super().hello() # 调用A类的方法 super() 无参的时候，函数只能用在对象的方法里，不能在外面用

b = B()
# b.hello() # 调用B类的hello
# super(B, b).hello() # 调用A类的hello
b.say()
