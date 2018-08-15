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


# def mysort(x):
#     return x['age']
def mysort(x):
    return x['score']


def output_student(L):
    line = "+------+------+------+"
    title = "| name | age | score |"
    print(line)
    print(title)
    print(line)

    for d in sorted(L, key = mysort): #reverse = True 逆序排列
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
    for y in range(0, len(L)):
        if m == L[y]['name']:
            del L[y]
    else:
        print("没有该学生！")


def show_menu():
    print("1)添加学生信息")
    print("2)显示学生信息")
    print("3)修改学生信息")
    print("4)删除学生信息")
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
        elif n == 'q':
            break

mian()









