def fibo(n):
    if n >= 1:
        yield 1
    if n >= 2:
        yield 1
    a, b = 1, 1
    for x in range(n - 2):
        x = a + b
        yield x
        a, b = b, x

L = [x for x in fibo(100)]
print(L)