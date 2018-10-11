try:
    f = open("data.bin", 'rb')
    b = f.read()  # 读取5个字节
    print("b的长度是：", len(b))
    print(b)
    f.close()
except Exception as e:
    print("Error")
