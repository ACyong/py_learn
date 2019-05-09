class Student(): # 创建一个类，用变量Student来绑定
    def __init__(slef, n, a, s):
        slef.set_infos(n, a, s)
        # slef.name = n
        # assert 0 <= a <= 140 , "年龄不在合法区间"
        # slef.age = a
        # slef.score = s


    def set_infos(slef, n, a, s):
        slef.name = n
        assert 0 <= a <= 140 , "年龄不在合法区间"
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
        stu = Student(n, a, s)
        L.append(stu)
    return L


def output_student(lst):
    for stu in lst:
        print(stu.get_infos())


docs = input_student()
output_student(docs) # 打印




