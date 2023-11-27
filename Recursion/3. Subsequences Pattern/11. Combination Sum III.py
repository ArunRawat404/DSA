def findCombinations(i, combinations, ans, k, n):
    if len(combinations) == k:
        if n == 0:
            ans.append(combinations.copy())
        return

    # We can use every element once only, so we will use the element greater than the previous elements.
    for i in range(i, 10):
        if i > n:
            break

        combinations.append(i)
        findCombinations(i + 1, combinations, ans, k, n - i)
        # Backtrack by removing the last added element.
        combinations.pop()


def combinationSum3(k, n):
    ans = []
    findCombinations(1, [], ans, k, n)
    return ans


k = 3
n = 9
print(combinationSum3(k, n))
