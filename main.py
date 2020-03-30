# a = [1, 1, 1, 1, 1, 2, 2, 2]
# a = [0, 0, 0, 0, 0, 0, 0]
# a = [1, 2, 3, 4, 5, 6]
a = [int(i) for i in input().split()]
a.sort()
b = []
# c = []
if a[0] == a[-1] and len(a) != 1:
    b.append(a[0])
for i in range(0, len(a) - 1):
    if a[i] == a[i + 1] and a[i] != a[i - 1]:
        b.append(a[i])
    i += 1
# print(b)

for i in b:
    print(i, " ", end="")
