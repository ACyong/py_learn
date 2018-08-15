class Student():  # 创建一个类，用变量Student来绑定
    def set_infos(slef, n, a, s):
        slef.name = n
        assert 0 <= a <= 140, "年龄不在合法区间"
        slef.age = a
        slef.score = s

    def get_infos(slef):
        return "姓名：" + slef.name + \
               "年龄：" + str(slef.age) + \
               "成绩：" + str(slef.score)


def input_student():
    L = []
    while True:
        n = input("请输入姓名：")
        if not n:
            break
        a = int(input("请输入年龄："))
        s = int(input("请输入年龄："))

        # 此处创建学生对象并添加到列表L中
        stu = Student()
        stu.set_infos(n, a, s)
        # stu.name = n # 添加实例变量
        # stu.age = a
        # stu.score = s
        L.append(stu)  # 加到列表L中

    return L  # 返回记录对象的列表


docs = input_student()
print(docs)


def output_student(lst):
    for stu in lst:
        # print("姓名：", stu.name, "年龄：", stu.age, "成绩：", stu.score)
        print(stu.get_infos())


output_student(docs)  # 打印
