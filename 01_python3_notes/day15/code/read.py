try:
    f = open("data.txt", 'rt')
    s = f.readline()
    print("s的长度是：", len(s))
    print("s的内容是：", s)
    s = f.readline()
    print("s的长度是：", len(s))
    print("s的内容是：", s)

except :
    raise e

