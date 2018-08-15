def make_raise():
    print("start")
    raise ZeroDivisionError("假的零除")
    print("end")


try:
    make_raise()
except ZeroDivisionError as err:  # err绑定错误对象
    print("出现错误")
    print("错误类型：", err)
