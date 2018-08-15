def fun(x):
    if x == 1:
        return 1
    return x * fun(x-1)

print(sum(map(fun, range(1, 21))))