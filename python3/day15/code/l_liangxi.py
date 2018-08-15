def get_text():
    L = []

    while True:
        s = input("请输入：")
        if s == '':
            break
        L.append(s)
    return L

# def print_by_zip(lst):
#     for x in zip(range(1, len(lst) + 1), lst):
#         line_no, s = x
#         print("第%d行：%s" % (line_no, s))

def print_by_zip(lst):
    for x in enumerate(lst, 1):
        line_no, s = x
        print("第%d行：%s" % (line_no, s))


L = get_text()
print_by_zip(L)