def rotate(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    for row in range(row_len):
        for col in range(row, col_len):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in matrix:
        row.reverse()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
print(matrix)
