# def get_score():
#     try:
#         score = int(input("输入学生成绩:"))
#     except:
#         print("程序错误")
#         score = 0
#     if score < 0 or score > 100:
#         raise ValueError("值不在范围！")
#     return score

# print(get_score())

def get_score():
    score = int(input("输入学生成绩:"))
    if score < 0:
        raise ValueError("成绩小于零")
    if score > 100:
        raise ValueError("成绩大于零")
    return score

while True:
    try:
        score = get_score()
        break
    except ValueError as err:
        print("有错误发生：", err)

print("学生的成绩是：", score)
