def generateBinaryStrings(str, ans, index, subsequence):
    if index == len(str):
        ans.append(subsequence)
        return

    if str[index] != "?":
        generateBinaryStrings(str, ans, index + 1, subsequence + str[index])
    else:
        generateBinaryStrings(str, ans, index + 1, subsequence + "0")
        generateBinaryStrings(str, ans, index + 1, subsequence + "1")


def binaryStrings(str):
    ans = []
    generateBinaryStrings(str, ans, 0, "")
    return ans


str = "1??0?101"
print(binaryStrings(str))
