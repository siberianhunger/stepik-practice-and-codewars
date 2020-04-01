column = []
matrix = []
modified_matrix = []
p = 0
while 1:
    column = [str(i) for i in input().split()]
    # print(column)
    if column[0] == 'end':
        break
    matrix.append(list(map(int, column)))
    p += 1
for i in range(len(matrix)):
    modified_matrix.append([])
    for j in range(len(matrix[i])):
        modified_matrix[i].append(0)
# print(modified_matrix)
# print(matrix)
# for i in matrix:
#     print("\n")
#     for j in i:
#         print(j, end=' ')
# print('')
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        # print(i, j)
        if i != len(matrix) - 1 and j == len(matrix[i]) - 1:
            modified_matrix[i][j] = matrix[i - 1][j] + matrix[i+1][j] + matrix[i][j - 1] + matrix[i][0]
        elif i == len(matrix) - 1 and j != len(matrix[i]) - 1:
            modified_matrix[i][j] = matrix[i - 1][j] + matrix[0][j] + matrix[i][j - 1] + matrix[i][j + 1]
        elif i == len(matrix) - 1 and j == len(matrix[i]) - 1:
            modified_matrix[i][j] = matrix[i - 1][j] + matrix[0][j] + matrix[i][j - 1] + matrix[i][0]
        else:
            modified_matrix[i][j] = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][j + 1]

        # print(i, j, " modified matrix", modified_matrix[i][j])
# print('')
for i in modified_matrix:
    print('\n', end='')
    for j in i:
        print(j, end=" ")
# for i in matrix:
#     print('\n')
#     for j in i:
#         print(j, end=" ")
