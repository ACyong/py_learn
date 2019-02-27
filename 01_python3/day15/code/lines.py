try:
    f = open("data.txt", "rt")
    L = f.readlines()
    print(L)
    f.close()
except :
    raise e