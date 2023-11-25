def findCombination(index, candidates, target, subsequence, ans):
    if target == 0:
        ans.append(subsequence.copy())
        return

    for i in range(index, len(candidates)):
        # to make sure unique subsequence are chosen
        if i > index and candidates[i] == candidates[i - 1]:
            continue

        # not possible as sum of subsequence will exceed target
        if candidates[i] > target:
            break

        subsequence.append(candidates[i])
        findCombination(i + 1, candidates, target - candidates[i], subsequence, ans)
        subsequence.pop()


def combinationSum2(candidates, target):
    ans = []
    candidates.sort()
    findCombination(0, candidates, target, [], ans)
    return ans


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum2(candidates, target))
