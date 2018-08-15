def fibs(n):
    if (n==1 or n==2):
        return 1
    return fibs(n-2) + fibs(n-1)

print(fibs(10))
