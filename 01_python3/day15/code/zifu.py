try:
    f = open("data.txt", "rt")
    L = f.read(3)
    print(L)
    f.close()
except :
    raise e