L = []

while True:
    s = input("请输入：")
    if s == '':
        break
    L.append(s)


for no, n in enumerate(L, 1):  # (等同于序列赋值)
    print('第',no,'行', n)