# def power(x):
# 	return x**2
# L = []
# mit = map(power, range(1, 10)) #返回一个新的可迭代对象，此可迭代对象可以生成一系列的平方
# for x in mit:
# 	L.append(x)
# print(L)

# L = [x for x in map(power, range(1, 10))]
# print(L)

# 生成一个可迭代对象，此可迭代对象可以生成1**4，2**3，4**1
def mypow(x, y):
	return x ** y
L = [x for x in map(mypow, range(1, 5), range(4, 0, -1))]
print(L)