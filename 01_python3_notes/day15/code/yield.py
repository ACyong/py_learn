def myyield():
    """此函数内因为有yield语句，此函数将作为生成器函数使用
    """
    yield 2
    yield 3
    yield 5
    yield 7

for x in myyield():
    print(x)