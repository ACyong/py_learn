# def fibonacci(n):
#     L = [1, 1]
#     for x in range(n - 2):
#         s = 0
#         s = (L[x] + L[x + 1])
#         L.append(s)
#     for y in L:
#         yield y


# L = [x for x in fibonacci(7)]
# print(L)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    # return "done"


# f = fib(10)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

g = fib(6)
while True:
    try:
        x = next(g)
        print("g", x)
    except Exception as e:
        print("Generator return value:", e.value)
        break
