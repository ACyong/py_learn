class Human:
    """人类，把人类的行为加在此类中"""
    def say(self, what):
        print("说：", what)

    def run(self, speed):
        print("可以以%d km/h的速度行走" % speed)


h1 = Human()
h1.say("今天晴天")
h1.run(5)

class Student(Human):
    """子类可以直接调用父类的方法"""
    def study(self, what):
        print("正在学习：",what)

s1 = Student()
s1.say("今天晴天")
s1.run(5)
s1.study("python")







