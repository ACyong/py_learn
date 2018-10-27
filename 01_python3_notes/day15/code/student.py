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


def mysort_score(x):
    return x['score']
def mysort_age(x):
    return x['age']


def output_student(L):
    line = "+------+------+------+"
    title = "| name | age | score |"
    print(line)
    print(title)
    print(line)

    for d in L:
        s = '|%s|%s|%s|' % (d['name'].center(6),
                            str(d['age']).center(6), str(d['score']).center(6))
        print(s)
    print(line)


def output_student_ascore(L):
    line = "+------+------+------+"
    title = "| name | age | score |"
    print(line)
    print(title)
    print(line)
    for d in sorted(L, key = mysort_score): #reverse = True 逆序排列
        s = '|%s|%s|%s|' % (d['name'].center(6),
                            str(d['age']).center(6), str(d['score']).center(6))
        print(s)
    print(line)


def output_student_dscore(L):
    line = "+------+------+------+"
    title = "| name | age | score |"
    print(line)
    print(title)
    print(line)
    for d in sorted(L, key = mysort_score, reverse = True):
        s = '|%s|%s|%s|' % (d['name'].center(6),
                            str(d['age']).center(6), str(d['score']).center(6))
        print(s)
    print(line)


def output_student_aage(L):
    line = "+------+------+------+"
    title = "| name | age | score |"
    print(line)
    print(title)
    print(line)
    for d in sorted(L, key = mysort_age):
        s = '|%s|%s|%s|' % (d['name'].center(6),
                            str(d['age']).center(6), str(d['score']).center(6))
        print(s)
    print(line)


def output_student_dage(L):
    line = "+------+------+------+"
    title = "| name | age | score |"
    print(line)
    print(title)
    print(line)
    for d in sorted(L, key = mysort_age, reverse = True):
        s = '|%s|%s|%s|' % (d['name'].center(6),
                            str(d['age']).center(6), str(d['score']).center(6))
        print(s)
    print(line)


def change_student(L):
    m = input("输入要修改的学生姓名：")
    for x in L:
        if m == x['name']:
            x['age'] = input("修改学生%s年龄信息:" % x['name'])
            x['score'] = input("修改学生%s分数信息:" % x['name'])


def del_student(L):
    m = input("输入要删除的学生姓名：")
    for y in L:
        if m == y['name']:
            L.remove(y)
    else:
        print("没有该学生！")


def csv(L, filename = 'infos.csv'):
    f = open(filename, "bw")
    for d in L:
        s = '%s, %s, %s' % (d['name'], str(d['age']), str(d['score'])) + "\r\n"
        s = s.encode(encoding = "gbk")
        f.write(s)
        # print(s, file = filename)
    f.close()
    print("存储成功！")


def show_menu():
    print("1)添加学生信息")
    print("2)显示学生信息")
    print("3)修改学生信息")
    print("4)删除学生信息")
    print("5)按分数升序排")
    print("6)按分数降序排")
    print("7)按年龄升序排")
    print("8)按年龄降序排")
    print("9)存储学生信息")
    print("0)输出学生信息")
    print("q)退出")


def mian():
    docs = [] # 添加学生信息
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
                output_student_ascore(docs)
            else:
                print("学生信息为空！")
                continue
        elif n == '6':
            if docs:
                output_student_dscore(docs)
            else:
                print("学生信息为空！")
                continue
        elif n == '7':
            if docs:
                output_student_aage(docs)
            else:
                print("学生信息为空！")
                continue
        elif n == '8':
            if docs:
                output_student_dage(docs)
            else:
                print("学生信息为空！")
                continue
        elif n == '9':
            if docs:
                csv(docs)
            else:
                print("学生信息为空！")
                continue
        elif n == '10':
                output_student_dage(docs)

        elif n == 'q':
            break

mian()









