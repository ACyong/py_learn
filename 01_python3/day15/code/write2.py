
try:
    f = open("data2.txt", 'w')
    f.write("hello")
    f.write("hello")
    f.close()

except :
    print("文件打开失败")