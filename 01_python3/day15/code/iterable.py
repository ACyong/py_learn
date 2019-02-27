L = [2,3,5,7]

for x in L:
    print(x)

print("------------------")

it = iter(L)
while True:
    try:
        print(next(it))
    except StopIteration:
        break