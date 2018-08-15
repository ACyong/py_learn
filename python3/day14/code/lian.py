def height(h, s):
    l = 0
    for x in range(1,s+1):
        l += (h * 1.5)
        h /= 2
    return h,l


print(height(100, 10))