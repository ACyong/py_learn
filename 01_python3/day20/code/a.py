def a(n):
    return n


def b():
    n = 5
    return a(n)


n = 4
print(a(n))

print(b())
