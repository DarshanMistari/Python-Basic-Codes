# Matrix 4 * 5

matrix = [
    [5, 2, 7, 3, 9],
    [2, 4, 6, 7, 5],
    [1, 3, 5, 6, 4],
    [8, 6, 7, 5, 3]
]

rows = len(matrix)
columns = len(matrix[0])

for i in range(0,rows):
    for j in range(0 ,columns):
        print(matrix[i][j],end=" ")
    print()