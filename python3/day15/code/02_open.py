f = open("python.txt", "r")

count = 0
for i in f:
    if count == 9:
        print("-----------")
        count += 1
        break
    print(i)
    count += 1

f.close()
# print(f.closed())




