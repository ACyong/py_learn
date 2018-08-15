import random as R

def reduce(L, w):
    for x in w:
        L.pop(L.index(x))
    return L

L = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
H = ['\u2660', '\u2663', '\u2665', '\u2666']

P = ['X','x']
for x in H:
    for y in L:
        s = x + y
        P.append(s)

R.shuffle(P)

i = 0
L2 = []
while i < 2:
    if len(P) > 17:
        w = R.sample(P, 17) # 从序列中选择n个随机且不重复的元素
        L2.append(w)
        P = reduce(P, w)
        print(w)
        input()
    else:
        break
print(P)
