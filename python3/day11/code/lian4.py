s = "ABCDEFG"
L = [1, 2, 3, 4, 5, 6, 7]
def fun(x, y):
	return x+str(y)
L2 = []
for x in map(fun, s, L):
    L2.append(x)
print(L2)