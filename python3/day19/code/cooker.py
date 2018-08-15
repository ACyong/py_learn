class Cooker:
    def __init__(self, n):
        self.name = n

    def open_gas(self):
        print(self.name, "正在打开天然气")

    def close_gas(self):
        print(self.name, "正在关闭天然气")

    def do_works(self):
        print(self.name, "开始制作甜饼")
        n = int(input("请输入甜饼数："))
        print(self.name, "已经制作了", n, "个小甜饼")

    def __enter__(self):
        self.open_gas()
        return self

    def __exit__(self, t, v, tb): # 离开with语句一定会执行此方法
        """t为异常类型，没有异常时为None，
        有异常时绑定异常对象的类型"""
        self.close_gas()
        if t is None:
            print("没有异常")
        else:
            print("有异常发生，异常类型为", t)

# try:
#     c = Cooker("lw")
#     c.open_gas()
#     c.do_works()
# finally:
#     c.close_gas()

with Cooker("qjd") as c:
    c.do_works()

