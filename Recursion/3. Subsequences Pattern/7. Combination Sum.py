def combinationSum(index, target, subsequence):
    if index == len(candidates):
        if target == 0:
            ans.append(subsequence.copy())
        return

    if candidates[index] <= target:
        subsequence.append(candidates[index])
        # add current element
        combinationSum(index, target - candidates[index], subsequence)
        # remove element when recursion calls end
        subsequence.pop()

    # increasing the index only
    combinationSum(index + 1, target, subsequence)


candidates = [7, 14, 2, 6, 5]
target = 18
ans = []
combinationSum(0, target, [])
print(ans)
