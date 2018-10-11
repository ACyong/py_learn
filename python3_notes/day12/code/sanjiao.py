def L(num):
    L = [[1]]

    for i in range(2, num + 1):
        L.append([1] * i)
        for j in range(1, i - 1):
            L[i - 1][j] = L[i - 2][j] + L[i - 2][j - 1]

    return L


def printL(L, width):
    column = len(L[-1]) * width
    for lst in L:
        result = []
        for contents in lst:
            result.append('{0:^{1}}'.format(str(contents), width))
        print('{0:^{1}}'.format(''.join(result), column))


num = int(input('行数：'))
L = L(num)

width = len(str(L[-1][len(L[-1]) // 2])) + 3
printL(L, width)
