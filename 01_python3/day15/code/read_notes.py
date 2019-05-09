# L = []
# try:
#     f = open("mynotes.txt", "rt")
#     while True:
#         s = f.readline()
#         if s == '':
#             break
#         L.append(s.rstrip())
#     for x in enumerate(L, 1):
#         print(x)
# except :
#     pass



def read_notes():
    L = []
    try:
        f = open("mynotes.txt", "rt")
        while True:
            s = f.readline()
            if s:
                L.append(s.strip())
            else:
                break
        f.close()
    except :
        print("打开文件失败！")
    return L

def print_enumerate(lst):
    for x in enumerate(lst, 1):
        line_no, s = x
        print("第%d行：%s" % (line_no, s))


L = read_notes()
print_enumerate(L)






