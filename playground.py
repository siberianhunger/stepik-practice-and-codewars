a = int(input())
b = []
p = a
while p != 0:
    for i in range(0, p):
        b.append(p)
    p -= 1
b = list(reversed(b))
for i in range(0, a):
    print(b[i], end=' ')
