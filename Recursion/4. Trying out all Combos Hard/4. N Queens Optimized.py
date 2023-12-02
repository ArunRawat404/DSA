# Time Complexity: Exponential in nature since we are trying out all ways, to be precise it is O(N! * N).
# Space Complexity: O(N)


def solve(col, board, ans, left_row, upper_diagonal, lower_diagonal, n):
    if col == n:
        ans.append(board[:])
        return

    for row in range(n):
        if (
            left_row[row] == 0
            and lower_diagonal[row + col] == 0
            and upper_diagonal[n - 1 + col - row] == 0
        ):
            board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
            left_row[row] = 1
            lower_diagonal[row + col] = 1
            upper_diagonal[n - 1 + col - row] = 1
            solve(col + 1, board, ans, left_row, upper_diagonal, lower_diagonal, n)
            board[row] = board[row][:col] + "." + board[row][col + 1 :]
            left_row[row] = 0
            lower_diagonal[row + col] = 0
            upper_diagonal[n - 1 + col - row] = 0


def solveNQueens(n):
    ans = []
    board = ["." * n for _ in range(n)]
    left_row = [0] * n
    upper_diagonal = [0] * (2 * n - 1)
    lower_diagonal = [0] * (2 * n - 1)
    solve(0, board, ans, left_row, upper_diagonal, lower_diagonal, n)
    return ans


n = 4
print(solveNQueens(n))
