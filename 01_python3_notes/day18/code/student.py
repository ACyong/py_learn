import student_class as student


def input_student():
    L = []
    while True:
        n = input("请输入学生姓名：")
        if not n:
            break
        a = int(input("请输入学生年龄："))
        s = int(input("请输入学生成绩："))
        d = student.Student(n, a, s)
        L.append(d)
    return L


def output_student(L):
    line = "+------+------+------+"
    title = "| name | age | score |"
    print(line)
    print(title)
    print(line)

    for d in L:
        s = d.get_infos()
        print(s)
    print(line)


def show_menu():
    print("1)添加学生信息")
    print("2)显示学生信息")
    print("3)修改学生信息")
    print("4)删除学生信息")
    print("5)按分数升序排")
    print("6)按分数降序排")
    print("7)按年龄升序排")
    print("8)按年龄降序排")
    print("9)存储信息csv")
    print("0)输出信息csv")
    print("a)存储信息txt")
    print("b)输出信息txt")
    print("q)退出")


def change_student(L):
    m = input("输入要修改的学生姓名：")
    for x in L:
        if m == x.name:
            x.age = input("修改学生%s年龄信息:" % x.name)
            x.score = input("修改学生%s分数信息:" % x.name)


def del_student(L):
    m = input("输入要删除的学生姓名：")
    for y in L:
        if m == y.name:
            L.remove(y)
    else:
        print("没有该学生！")


def csv(L, filename='/Users/shouei/python/pbase/day18/code/infos.csv'):
    f = open(filename, "bw")
    for d in L:
        s = '%s, %s, %s' % (d.name, str(d.age), str(d.score)) + "\r\n"
        s = s.encode(encoding="gbk")
        f.write(s)
        # print(s, file = filename)
    f.close()
    print("存储成功！")


def read_from_csv(filename="/Users/shouei/python/pbase/day18/code/infos.csv"):
    L = []
    f = open(filename, 'br')
    while True:
        d = f.readline()
        if not d:
            break
        d = d.decode('gbk')
        d.rstrip()
        n_a_s = d.split(',')
        n, a, s = n_a_s
        a = int(a)
        s = int(s)
        L.append(student.Student(n, a, s))
    f.close()
    return L


def save_to_txt(docs, filename='/Users/shouei/python/pbase/day18/code/si.txt'):
    try:
        f = open(filename, 'w')
        for d in docs:
            s = d.get_file_info()
            f.write(s + '\n')
        f.close()
        print("保存成功")
    except:
        print("操作文件失败")


def read_from_text(filename='/Users/shouei/python/pbase/day18/code/si.txt'):
    f = open(filename)
    L = []
    while True:
        s = f.readline()
        if not s:
            break
        s = s.rstrip()
        name_age_score = s.split(',')
        print(name_age_score)
        n, a, s = name_age_score
        a = int(a)
        s = int(s)
        L.append(student.Student(n, a, s))
    f.close()
    return L


def mian():
    docs = []  # 添加学生信息
    while True:
        show_menu()
        n = input()
        if n == '1':
            lst = input_student()
            docs.extend(lst)
        elif n == '2':
            output_student(docs)
        elif n == '3':
            if docs:
                change_student(docs)
            else:
                print("学生信息为空！")
                continue
        elif n == '4':
            if docs:
                del_student(docs)
            else:
                print("学生信息为空！")
                continue
        elif n == '5':
            if docs:
                def k(d):
                    return d.score
                lst = sorted(docs, key=k, reverse=True)
            else:
                print("学生信息为空！")
                continue
        elif n == '6':
            if docs:
                def k(d):
                    return d.score
                lst = sorted(docs, key=k)
            else:
                print("学生信息为空！")
                continue
        elif n == '7':
            if docs:
                def k(d):
                    return d.age
                lst = sorted(docs, key=k, reverse=True)
            else:
                print("学生信息为空！")
                continue
        elif n == '8':
            if docs:
                def k(d):
                    return d.age
                lst = sorted(docs, key=k)
            else:
                print("学生信息为空！")
                continue
        elif n == '9':
            if docs:
                csv(docs)
            else:
                print("学生信息为空！")
                continue
        elif n == '0':
            docs = read_from_csv()
            output_student(docs)
        elif n == 'a':
            save_to_txt(docs)
        elif n == 'b':
            docs = read_from_text()
            output_student(docs)
        elif n == 'q':
            break

mian()










