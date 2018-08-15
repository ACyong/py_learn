import time

def f(n):
	print(n)
	time.sleep(1)
	if n >= 10: #设置返回条件
		return
	f(n+1)

f(1)