# Approach -> Start from Cell (0, m - 1) and the corresponding row and column will be in increasing order so we can use binary search to eliminate down one half
# Complexity -> O(n + m)


def searchMatrix(matrix, target):
    row_len = len(matrix)
    col_len = len(matrix[0])
    row = 0
    col = col_len - 1

    while row < row_len and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1

    return False


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
target = 5
print(searchMatrix(matrix, target))
