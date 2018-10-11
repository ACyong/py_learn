def get_yhlist(fristline:"起始行", layer:"整数层数"):
    yhlist = []
    L = fristline

    for _ in range(layer):
        yhlist.append(L)
        L2 = [L[0]]
        # 如下循环把中间的数据计算出来
        for x in range(len(L) - 1):
            L2.append(L[x] + L[x+1])
        L2.append(L[-1]) # 将最后一个加入到末尾
        L = L2

    return yhlist


def get_yhstring(lst:"yhlist"):

    string_list = []
    for x in lst:
        L = [str(y) for y in x]
        s = ' '.join(L)
        string_list.append(s)
        # print(s)

    return string_list


def output(str_list):
    max_len = len(str_list[-1])
    for x in str_list:
        print(x.center(max_len))


yhlist = get_yhlist([1], 6)
str_list = get_yhstring(yhlist)
output(str_list)



