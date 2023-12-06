# Time Complexity: O(9(n ^ 2)), in the worst case, for each cell in the n2 board, we have 9 possible numbers
# Space Complexity: O(1), since we are refilling the given board itself, there is no extra space required, so constant space complexity.


def isValid(board, row, col, digit):

    for i in range(9):
        # to check if digit is already present in row
        if board[row][i] == digit:
            return False

        # to check if digit is already present in column
        if board[i][col] == digit:
            return False

        # to check if digit is already present in 3 * 3 sub-grid
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == digit:
            return False

    return True


def solveSudoku(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ".":
                for digit in "123456789":
                    if isValid(board, i, j, digit):
                        board[i][j] = digit

                        if solveSudoku(board):
                            return True
                        board[i][j] = "."

                return False

    return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

solveSudoku(board)
print(board)
