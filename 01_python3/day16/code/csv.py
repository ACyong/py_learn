# 练习：写程序，从键盘输入多个人的年龄，姓名，成绩,当姓名为空时结束，保存为二进制文件
#      格式为：姓名，年龄，成绩 \r\n
#      文件名为：infos.csv
#      要求文件内部编码格式为：
#      “gbk”
#      b = s.encode('gbk')
#      f.write(b)
#      尝试在windows下用Excel 打开infos.csv文件


def input_student():
    L = []
    while True:
        n = input("请输入学生姓名：")
        if not n:
            break
        a = int(input("请输入学生年龄："))
        s = int(input("请输入学生成绩："))
        d = {"name": n, "age": a, "score": s}
        L.append(d)
    return L

def csv(L, filename = 'infos.csv'):
    f = open(filename, "bw")
    for d in L:
        s = '%s, %s, %s' % (d['name'], str(d['age']), str(d['score'])) + "\r\n"
        s = s.encode(encoding = "gbk")
        f.write(s)
    f.close()

L = input_student()
csv(L)




