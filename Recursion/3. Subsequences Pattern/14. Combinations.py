def findCombinations(i, combinations, ans, k, n):
    if len(combinations) == k:
        ans.append(combinations.copy())
        return

    for i in range(i, n + 1):
        combinations.append(i)
        findCombinations(i + 1, combinations, ans, k, n)
        combinations.pop()


def combine(k, n):
    ans = []
    findCombinations(1, [], ans, k, n)
    return ans


k = 2
n = 4
print(combine(k, n))
