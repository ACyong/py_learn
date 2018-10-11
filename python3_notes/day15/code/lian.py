# lian.py
# 练习：写一个程序，从键盘读入一些字符串，当输入空行时结束
#      将以上读入内容写入文件“input.txt”中（）要求：键盘操作和文件内容一致

try:
    f = open("input.txt", "w")

    while True:
        s = input("输入：")
        if s:
            f.write(s + "\n")
        else:
            break
    f.close()
except :
    raise e