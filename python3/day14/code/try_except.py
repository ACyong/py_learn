# 此实例演示异常的处理流程

def div_apple(n):
    print("现在有", n, "个苹果，请问分给几个人")
    s = input("请输入人数：")
    d = int(s)
    print("每个人分了", n/d, "个苹果")

def fn(n):
    print("fn调用前")
    div_apple(n)
    print("fn调用后")

# 此函数可能出现错误并进入异常状态
# try:
#     fn(10)
# except ZeroDivisionError as e:
#     print("零除错误，苹果没分成功")
# except ValueError as e:
#     print("发生值错误，已从异常状态转为正常状态")
# print("程序结束")

# try:
#     fn(10)
# except (ZeroDivisionError, ValueError):
#     print("两个错误一样的处理")
# print("程序结束")

# try:
#     fn(10)
# except ZeroDivisionError as e:
#     print("零除错误，苹果没分成功")
# except:
#     print("发生其他类型错误，已从异常状态转为正常状态")
# print("程序结束")

try:
    fn(10)
except ZeroDivisionError as e:
    print("零除错误，苹果没分成功")
else:
    print("没有异常发生，才会执行")
print("程序结束")

try:
    fn(10)
except ZeroDivisionError as e:
    print("零除错误，苹果没分成功")
finally:
    print("是否发生异常，都会被输出")
print("程序结束")











