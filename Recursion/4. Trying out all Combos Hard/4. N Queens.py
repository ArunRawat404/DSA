# Time Complexity: Exponential in nature, since we are trying out all ways. To be precise it goes as O(N! * N) nearly.
# Space Complexity: O(N^2)


def isPlacingQueenPossible(row, col, board, n):
    # check upper element
    dup_row = row
    dup_col = col

    while row >= 0 and col >= 0:
        if board[row][col] == "Q":
            return False
        row -= 1
        col -= 1

    col = dup_col
    row = dup_row
    while col >= 0:
        if board[row][col] == "Q":
            return False
        col -= 1

    # check row
    row = dup_row
    col = dup_col
    while row < n and col >= 0:
        if board[row][col] == "Q":
            return False
        row += 1
        col -= 1

    return True


def solve(col, board, ans, n):
    if col == n:
        ans.append(board.copy())
        return

    for row in range(n):
        if isPlacingQueenPossible(row, col, board, n):
            # as string is immutable we have to slice string and concatenate them
            board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
            solve(col + 1, board, ans, n)
            board[row] = board[row][:col] + "." + board[row][col + 1 :]


def solveNQueens(n):
    ans = []
    board = ["." * n for _ in range(n)]
    solve(0, board, ans, n)
    return ans


n = 4
print(solveNQueens(n))
