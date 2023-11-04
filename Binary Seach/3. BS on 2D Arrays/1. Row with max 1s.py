def rowWithMax1s(matrix):
    ans = -1
    first_one_pos = -1
    # traverse the rows:
    for row in range(len(matrix)):
        start = 0
        end = len(matrix[0]) - 1

        while start <= end:
            mid = start + (end - start) // 2
            # current position have 1
            if matrix[row][mid] == 1:
                # if it's first 1 or got a 1 left to previous 1
                if (ans == -1) or (first_one_pos > mid):
                    ans = row
                    first_one_pos = mid
                    if first_one_pos == 0:
                        return ans
                # search in left half for more 1s
                end = mid - 1
            # search on right half
            else:
                start = mid + 1
    return ans


matrix = [[0, 1, 1], [0, 0, 1], [0, 0, 0]]
print(rowWithMax1s(matrix))
