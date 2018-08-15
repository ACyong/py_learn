def get_age():
    a = input("请输入年龄：")
    a = int(a) # ValueError错误
    assert a < 150, "年龄太大了"
    assert a > 0, "还没出生"
    return a

while True: # 循环读入解决NameValue错误
    try:
        # age = 0 # 默认值解决NameValue错误
        age = get_age()
        break
    except AsertiongError as e:
        print("发生年龄值不合法的错误，", e)
    except ValueError as e:
        print("发生输入值不能转为整数的错误", e)

print("您输入的年龄是：", age)




















