# Approach ->  flattening the 2D matrix into 1D and using // and % operator to get row and col values


def searchMatrix(matrix, target):
    row_len = len(matrix)
    col_len = len(matrix[0])

    start = 0
    end = row_len * col_len - 1
    while start <= end:
        mid = start + (end - start) // 2
        row = mid // col_len
        col = mid % col_len
        print(mid, matrix[row][col])
        if matrix[row][col] == target:
            return True

        elif matrix[row][col] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
target = 8
print(searchMatrix(matrix, target))
