

try:
    f = open("../../day18/code/si.txt")
    try:
        while True:
            x = f.readline()
            # 3 / 0 # 故意制造异常
            if not x:
                break
            print(x.strip())
    finally:
        f.close() # 保存关闭文件这件事一定会被执行

except IOError:
    print("打开文件失败！")

