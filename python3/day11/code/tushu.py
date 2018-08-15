L = [{"name":"Python", "price":58, "pages":866},
{"name":"C", "price":98, "pages":982},
{"name":"C++", "price":56, "pages":1024},
{"name":"Java", "price":79, "pages":691}
]
def fun(x):
	return x['price']
L6 = sorted(L, key = fun)
def show_books(lst):
	for x in lst:
		print("%10s %3d %5d" % (x['name'],x['price'],x['pages']))
show_books(L6)