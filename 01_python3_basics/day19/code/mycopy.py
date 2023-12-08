src_file = input("请输入源文件：")
dst_file = input("请输入目标文件：")

try:
    with open(src_file, 'rb') as fr, open (dst_file, 'wb') as fw:
        while True:
            b = fr.read(4096) # 每次读取4K个字节
            if not b: # 到达文件尾
                break
            fw.write(b)

except:
    print("复制文件失败")
else:
    print("赋值文件结束")

