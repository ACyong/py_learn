import random as R

x = R.randrange(1, 101)
c = 0
while True:
    y = int(input("输入一个数："))
    if x == y:
        print("猜对了")
        break
    elif x < y:
        print("猜大了")
    elif x > y:
        print("猜小了")
    c += 1
print("结束", c)
