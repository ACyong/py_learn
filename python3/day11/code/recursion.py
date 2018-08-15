import time

def f(n):
	if n <= 0: # 当n条件满足时终止调用终止自己，来终止递归调用
		return
	time.sleep(0.5)
	print("进入函数时：", n)
	f(n-1)
	print("退出函数前：", n)

f(3) #调用函数