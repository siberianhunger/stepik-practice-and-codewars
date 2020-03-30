s = 0
square_sum = 0
while 1:
    a = int(input())
    s += a
    square_sum += a * a
    if s == 0:
        break
print(square_sum)
