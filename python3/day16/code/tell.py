f = open("data.bin", 'rb')
print("当前文件读写位置为：", f.tell()) # 0
f.read(5)
print("当前文件读写位置为：", f.tell()) # 5
f.close()