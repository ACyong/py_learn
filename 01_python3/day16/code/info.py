# info.py
# 思考：写一个程序，读入一系列字符串，当输入空行结束，把所有字符串以二进制方式写入文件infos.bin

def get_text():
    L = []
    while True:
        s = input("请输入：")
        if s == '':
            break
        L.append(s)
    return L

# def info(L):
#     s = ''
#     for x in L:
#         s += x
#     return s.encode('utf-8')

# def write_bin(b_s):
#     # print(type(b_s))
#     try:
#         f = open("data3.txt", "bw")
#         f.write(b_s)
#         f.close()
#     except:
#         print("打开文件失败")

# L = get_text()
# b_s = info(L)
# write_bin(b_s)

def write_binary(L):
    f = open("data3.bin", "wb")
    for s in L:
        b = s.encode('utf-8')
        f.write(b)
        f.write(b'\n')
    f.close()

L = get_text()
write_binary(L)









