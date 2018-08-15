import sys
import time

for i in range(20):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.1)
else:
    print()


# f = open("data.txt", "w+")

# for i in range(20):
#     f.write("#")
#     f.flush()
#     time.sleep(0.1)
#     print(f.read(1))
