def isodd(x):
    return x % 2 == 0


# 生产偶数的列表
odds = [x for x in filter(isodd, range(20))]
print(odds)
