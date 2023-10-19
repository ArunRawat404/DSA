# Time Complexity -> O(n**2), Space Complexity -> O(n**2)


def generate(numRows):
    # generate a list of list with every element being 1
    pascal = [[1] * i for i in range(1, numRows + 1)]

    # No need to change first 2 rows
    for row in range(2, numRows):
        for col in range(1, row):
            pascal[row][col] = pascal[row - 1][col - 1] + pascal[row - 1][col]

    return pascal


numRows = 7
print(generate(numRows))
