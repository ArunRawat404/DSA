# Time Complexity: O(4^(m*n)), because on every cell we need to try 4 different directions.
# Space Complexity:  O(m*n) ,Maximum Depth of the recursion tree(auxiliary space).


def findPath(row, col, matrix, ans, path, visited):
    # we reached the destination
    if row == len(matrix) - 1 and col == len(matrix) - 1:
        ans.append(path)
        return

    # down
    if (
        row + 1 < len(matrix)
        and not visited[row + 1][col]
        and matrix[row + 1][col] == 1
    ):
        visited[row][col] = 1
        findPath(row + 1, col, matrix, ans, path + "D", visited)
        visited[row][col] = 0

    # left
    if col - 1 >= 0 and not visited[row][col - 1] and matrix[row][col - 1] == 1:
        visited[row][col] = 1
        findPath(row, col - 1, matrix, ans, path + "L", visited)
        visited[row][col] = 0

    # right
    if (
        col + 1 < len(matrix)
        and not visited[row][col + 1]
        and matrix[row][col + 1] == 1
    ):
        visited[row][col] = 1
        findPath(row, col + 1, matrix, ans, path + "R", visited)
        visited[row][col] = 0

    # up
    if row - 1 >= 0 and not visited[row - 1][col] and matrix[row - 1][col] == 1:
        visited[row][col] = 1
        findPath(row - 1, col, matrix, ans, path + "U", visited)
        visited[row][col] = 0


def ratMaze(matrix):
    ans = []
    # to mark with cell is visited or not
    visited = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]

    # if (0, 0) position is 1 only then proceed
    if matrix[0][0] == 1:
        findPath(0, 0, matrix, ans, "", visited)

    # no path found
    if len(ans) == 0:
        return [-1]
    return ans


matrix = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
print(ratMaze(matrix))
