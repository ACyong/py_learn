try:
    f = open("data2.bin", 'wb')
    # f.write('a') # 此时会出错，因为'a'为字符串
    f.write(b'a')
    f.write(b'b')
    f.write(b'\xe4')
    f.write(b'\xb8')
    f.write(b'\xab')
    f.close()
except TypeError:
    print('写文件错误')
except:
    print("文件打开失败！")