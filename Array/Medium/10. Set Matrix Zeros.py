# Better approach than brute force but not optimal

# def setZeroes(matrix):
#     row_len = len(matrix)
#     col_len = len(matrix[0])

#     row_arr = [0] * row_len
#     col_arr = [0] * col_len

#     for i in range(row_len):
#         for j in range(col_len):
#             if matrix[i][j] == 0:
#                 row_arr[i] = 1
#                 col_arr[j] = 1

#     for i in range(row_len):
#         for j in range(col_len):
#             if row_arr[i] == 1 or col_arr[j] == 1:
#                 matrix[i][j] = 0


# Optimal Approach
def setZeroes(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])

    col0 = 1

    # Traverse the matrix and mark 1st row & col accordingly
    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == 0:
                # mark ith row of col 0
                matrix[i][0] = 0
                # mark jth col of row 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    # Mark with 0 from (1, 1) to (row_len - 1, col_len - 1):
    for i in range(1, row_len):
        for j in range(1, col_len):
            if matrix[i][j] != 0:
                # check for col and row
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

    # Finally mark the 1st col & then 1st row
    if matrix[0][0] == 0:
        for j in range(col_len):
            matrix[0][j] = 0

    if col0 == 0:
        for i in range(row_len):
            matrix[i][0] = 0


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
setZeroes(matrix)
print(matrix)
