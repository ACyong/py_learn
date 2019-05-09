L = ["多发点饭\n", "sdfs\n", "dsfasdgas\n"]

try:
    f = open("data2.txt", 'w')
    f.writelines(L)
    f.close()
except IOError as e:
    print("有读写错误")
except :
    print("文件打开失败")