def mydeco(fn):  # 此函数为装饰器函数，可以用来装饰带有一个参数的函数
    def say_hello2(name):
        print("hello:", name)
    return say_hello2


@ mydeco
def say_hello(name):
    print("你好！", name)


# def say_hello2(name):
#     print("hello！", name)
# say_hello = say_hello2 此处可以用装饰器实现同样的功能
# say_hello = mydeco(say_hello) # 此处可以用装饰器语句 @
say_hello("小张")
say_hello("小王")
say_hello("小李")
say_hello("小魏")
# 假设say_hello在之后调用了很多次
