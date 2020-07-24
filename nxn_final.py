"""
Выведите таблицу размером n×n, заполненную числами от 1 до n^2
по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке,
как показано в примере (здесь n=5):

Sample Input:
5

Sample Output
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""

# n = int(input())
n = 6
arr = [[-1 for x in range(n)] for y in range(n)]


def print_array():
    for j in range(n):
        print('')
        for k in range(n):
            print(arr[j][k], " ", end='')


print_array()
horizontal_direction_flag = 1
vertical_direction_flag = 0
squared_num = n * n
stop_flag = 1
while stop_flag != squared_num:
    #  ->
    if horizontal_direction_flag and vertical_direction_flag == 0:
        for j in range(n):
            arr[j][k] = stop_flag
            stop_flag += 1
        horizontal_direction_flag = 0
        vertical_direction_flag = -1
    #  ↓
    elif horizontal_direction_flag == 0 and vertical_direction_flag == -1:
        for j in range(n):
            for k in range(n):
                arr[j][k] = stop_flag
                stop_flag += 1
        horizontal_direction_flag = 0
        vertical_direction_flag = -1

    #  <-
    elif horizontal_direction_flag and vertical_direction_flag:
        for j in range(n):
            for k in range(n):
                arr[j][k] = stop_flag
                stop_flag += 1
        horizontal_direction_flag = 0
        vertical_direction_flag = -1

    #  ↑
    elif horizontal_direction_flag and vertical_direction_flag:
        for j in range(n):
            for k in range(n):
                arr[j][k] = stop_flag
                stop_flag += 1
        horizontal_direction_flag = 0
        vertical_direction_flag = -1

    else:
        print("INTERNAL LOGIC ERROR")
print("\n***\n")
for j in range(n):
    for k in range(n):
        arr[j][k] = k + 1
print_array()
