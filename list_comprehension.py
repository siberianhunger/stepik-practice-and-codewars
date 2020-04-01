a = [int(i) for i in input().split()]
x = int(input())
b = []
for i in range(0, len(a)):
    if a[i] == x:
        b.append(i)
if not bool(b):
    print("Отсутствует")
else:
    for i in b:
        print(i, end=" ")
