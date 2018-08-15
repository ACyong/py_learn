names = ['Tom', 'Jerry', 'Spike', 'Tyke']
def fun(k): # 此函数内一定只有一个参数，此函数用于绑定元素，并返回此元素的排序依据
	return k[::-1]
L5 = sorted(names, key = fun)
print(L5)