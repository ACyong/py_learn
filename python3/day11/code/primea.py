def prime(x):
    for i in range(2, int(x**0.5 + 1)):
        if x % i == 0:
            return False
    else:
        return True


primes = [x for x in filter(prime, range(2, 100))]
print(primes)
