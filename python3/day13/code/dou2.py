import random as R

L = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
H = ['\u2660', '\u2663', '\u2665', '\u2666']
w1 = []
w2 = []
w3 = []

P = ['X','x']
for x in H:
    for y in L:
        s = x + y
        P.append(s)

R.shuffle(P)

i = 1
while i <= 17:
    w1.append(P.pop())
    w2.append(P.pop())
    w3.append(P.pop())
    i += 1

print(w1)
input()
print(w2)
input()
print(w3)
input()
print(P)
