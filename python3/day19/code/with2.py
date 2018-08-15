# 用with语句把si.txt的内容读出来
try:
    with open("../../day18/code/si.txt") as f:
        3 / 0
        for line in f:
            print(line.strip())
except:
    print("有异常发生")


print("f文件此时已经被关闭")

# try:
#     f = open("../../day18/code/si.txt")
#     try:
#         while True:
#             x = f.readline()
#             # 3 / 0 # 故意制造异常
#             if not x:
#                 break
#             print(x.strip())
#     finally:
#         f.close() # 保存关闭文件这件事一定会被执行

# except IOError:
#     print("打开文件失败！")

