matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
#
a = [[matrix[i][j] for i in range(len(matrix) - 1, -1, -1)] for j in range(len(matrix))]
# a = [matrix[i] for i in range(len(matrix)-1, -1, -1)]
print(a)
a = matrix
na = [[0]*3 for i in range(3)]
for j in range(len(matrix)):
    for i in range(len(matrix) - 1, -1, -1):
        na[j][2-i] = matrix[i][j]
        print(matrix[i][j])
q = [[matrix[i][j] for i in range(len(matrix) - 1, -1, -1)] for j in range(len(matrix))]
print(q)
