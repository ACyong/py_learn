# 此文件示意如何从seek.bin文件中读取中间的10个数字

f = open("seek.bin", "rb")
f.seek(5)  # 移动到相对于文件头为5的位置
f.seek(-15, 2)  # 相对于文件尾向前移动15的位置

f.read(2)
f.seek(3, 1)  # 相对于当前位置移动
b = f.read(10)
print(b)

f.close()
