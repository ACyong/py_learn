def myprimes(n, m):
    for y in range(n, m+1):
        for x in range(2, int(y**0.5)+1):
            if y % x == 0:
                break
        else:
            yield y


L = [x for x in myprimes(10, 20)]
print(L)