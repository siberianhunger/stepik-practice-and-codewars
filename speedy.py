a = [1, 2, 3, 4, 5, 6, 7, 2, 4]
p = -9223372036854775807
for i in range(0, len(a) - 1):
    if a[i] > p:
        p = a[i]
print(p)
