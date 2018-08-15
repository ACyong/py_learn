def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]

n=0
for t in triangles():
    print(t)
    n=n+1
    if n == 10:
        break
