import random as R

L = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
L1 = ['X', 'x']

L1.extend(map(lambda x: x+"\u2660", L))
L1.extend(map(lambda x: x+"\u2663", L))
L1.extend(map(lambda x: x+"\u2665", L))
L1.extend(map(lambda x: x+"\u2666", L))

R.shuffle(L1)
print(L1[0:17])
input()
print(L1[17:34])
input()
print(L1[34:51])
input()
print(L1[51:])