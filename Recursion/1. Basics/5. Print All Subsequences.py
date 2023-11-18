# Time Complexity : O(2**n)
# Space Complexity : O(n)
def printSubsequences(index, subsequence):
    if index >= len(array):
        print(subsequence)
        return

    # take or pick particular index into the sequence
    subsequence.append(array[index])
    printSubsequences(index + 1, subsequence)

    # not pick, or not take condition, this element is not added to your subsequence
    subsequence.pop()
    printSubsequences(index + 1, subsequence)


def Subsequences(index, subsequence, res):
    if index >= len(array):
        # append the actual instance of each modified subset `subset.copy()` instead of the reference which is pointing to the subset which gets modified.
        res.append(subsequence.copy())
        return

    # take or pick particular index into the sequence
    subsequence.append(array[index])
    Subsequences(index + 1, subsequence, res)

    # not pick, or not take condition, this element is not added to your subsequence
    subsequence.pop()
    Subsequences(index + 1, subsequence, res)


def getAllSubsequences():
    res = []
    subsequence = []
    Subsequences(0, subsequence, res)
    return res


array = [3, 1, 2]
printSubsequences(0, [])
print(getAllSubsequences())


# to get all subsequences of a string
def SubsequencesString(index, string, subsequence):
    if index == len(string):
        res.append(subsequence)
        return

    # take or pick particular index into the sequence
    subsequence += string[index]
    SubsequencesString(index + 1, string, subsequence)

    # not pick, or not take condition, this element is not added to your subsequence

    subsequence = subsequence[:-1]
    SubsequencesString(index + 1, string, subsequence)


string = "abc"
subsequence = ""
res = []
SubsequencesString(0, string, subsequence)
print(res)
