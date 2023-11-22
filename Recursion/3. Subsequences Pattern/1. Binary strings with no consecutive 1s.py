def generateString(n, index, string, ans, isOne):
    if index == n:
        ans.append(string)
        return

    # add "1" to string only if previous element is not "1"
    if isOne == False:
        generateString(n, index + 1, string + "1", ans, True)

    # add "0" to string
    generateString(n, index + 1, string + "0", ans, False)


n = 3
ans = []
generateString(n, 0, "", ans, False)
print(ans)
