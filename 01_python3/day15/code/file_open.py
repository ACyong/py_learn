
# f = open("data.txt") # 以只读方式打开
# print("文件打开成功！")
# f.close()

try:
    f = open("data.txt", 'rt') # 以只读方式打开,默认就是rt（‘r‘ read 和 ’t‘ txt）
    print("文件打开成功！")
    s = f.readline()
    print(s)
    f.close()
except:
    print("文件打开失败！！！")