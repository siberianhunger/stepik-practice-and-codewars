a = [1, 1, 1, 1, 1, 2, 2, 2]
# a = [int(i) for i in input().split()]
a.sort()
b = []
for i in range(0, len(a) - 1):
    if a[i] == a[i + 1]:
        b.append(a[i])
    i += 1
print(b)


def pepe(f: list):
    for sss in range(0, len(f) - 2):
        if f[sss] == f[sss + 1]:
            print(f)
            del f[sss]
            print(f, "sss")
    return f


pepe(b)
print(b)

# for i in range(0, len(b) - 1):
#     for c in range(0, len(b) - 1):
#         print(i, c, " \n")
#         if b[i] == b[c] and i != c:
#             b.pop(i)
#             print(b)
for i in b:
    print(i, " ", end="")
