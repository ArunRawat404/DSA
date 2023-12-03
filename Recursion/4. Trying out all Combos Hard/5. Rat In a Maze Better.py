# Time Complexity: O(4^(m*n)), because on every cell we need to try 4 different directions.
# Space Complexity:  O(m*n) ,Maximum Depth of the recursion tree(auxiliary space).


def findPath(row, col, matrix, ans, path, visited, direction_row, direction_col):
    # we reached the destination
    if row == len(matrix) - 1 and col == len(matrix) - 1:
        ans.append(path)
        return

    # based on d_row and d_col
    direction = "DLRU"

    for index in range(len(direction)):
        next_row = row + direction_row[index]
        next_col = col + direction_col[index]

        if (
            next_row >= 0
            and next_col >= 0
            and next_row < len(matrix)
            and next_col < len(matrix)
            and not visited[next_row][next_col]
            and matrix[next_row][next_col] == 1
        ):
            visited[row][col] = 1
            findPath(
                next_row,
                next_col,
                matrix,
                ans,
                path + direction[index],
                visited,
                direction_row,
                direction_col,
            )
            visited[row][col] = 0


def ratMaze(matrix):
    ans = []
    # to mark with cell is visited or not
    visited = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]

    # down, left, right, up
    direction_row = [+1, 0, 0, -1]
    direction_col = [0, -1, 1, 0]

    # if (0, 0) position is 1 only then proceed
    if matrix[0][0] == 1:
        findPath(0, 0, matrix, ans, "", visited, direction_row, direction_col)

    # no path found
    if len(ans) == 0:
        return [-1]
    return ans


matrix = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
print(ratMaze(matrix))
