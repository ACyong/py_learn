def myinteger(n):
    for x in range(0, n):
        yield x

it  = iter(myinteger(3))
print(next(it)) # 0
print(next(it)) # 1
print(next(it)) # 2

for x in myinteger(5):
    print(x) # 此处打印