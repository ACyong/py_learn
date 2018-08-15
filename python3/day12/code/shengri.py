import time

x = time.time()

g = time.mktime((1995, 1, 1, 0, 0, 0, 0, 0, 0))

print((x - g) // (3600 * 24) + 1)
