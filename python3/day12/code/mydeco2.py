# 实现用闭包来包裹原被装饰函数，可以在执行前和执行后加入自定义代码
def mydeco(fn):
    def f2(name): # 此时f2为闭包，因为f2调用了fn参数
        print("调用函数前。。。。")
        fn(name)
        print("调用函数后。。。。")
    return f2
@ mydeco
def say_hello(name):
    print("你好！", name)

say_hello("小张")
say_hello("小王")
say_hello("小李")
say_hello("小魏")

