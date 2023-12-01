# Time Complexity:  O(m*n*4^k), where “K” is the length of the word. And we are searching for the letter m*n times in the worst case. Here 4 in 4^k is because at each level of our decision tree we are making 4 recursive calls which equal 4^k in the worst case.
# Space Complexity: O(K), Where k is the length of the given words.


def exist(board, word):
    row_len = len(board)
    col_len = len(board[0])

    # reverse word if frequency of first word is larger than the last of word
    if word.count(word[0]) > word.count(word[-1]):
        word = word[::-1]

    def checkWord(row, col, ind):
        # Check if the word has been found.
        if ind == len(word):
            return True

        # if row or col is out of bound
        if row < 0 or col < 0 or row >= row_len or col >= col_len:
            return False

        # if current cell doesn't match the current letter
        if word[ind] != board[row][col]:
            return False

        # Store the value of the current cell.
        curr = board[row][col]
        # Mark the current cell as visited.
        board[row][col] = "#"

        # Recursively calling checkWord for the neighboring cells.
        res = (
            checkWord(row + 1, col, ind + 1)
            or checkWord(row - 1, col, ind + 1)
            or checkWord(row, col + 1, ind + 1)
            or checkWord(row, col - 1, ind + 1)
        )

        # Restore the original value of the current cell.
        board[row][col] = curr
        return res

    for row in range(row_len):
        for col in range(col_len):
            # only start the search when the cell letter match the first char of the word
            if board[row][col] == word[0] and checkWord(row, col, 0):
                return True

    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(exist(board, word))
