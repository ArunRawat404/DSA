def findSubset(index, subsequence, ans, nums):
    ans.append(subsequence.copy())

    for i in range(index, len(nums)):
        # skip duplicates
        if i > index and nums[i] == nums[i - 1]:
            continue

        subsequence.append(nums[i])
        findSubset(i + 1, subsequence, ans, nums)
        subsequence.pop()


# another solution
def backtrack(index, subsequence, ans, nums):
    if index == len(nums):
        ans.append(subsequence.copy())
        return

    subsequence.append(nums[index])
    # pick
    backtrack(index + 1, subsequence, ans, nums)
    subsequence.pop()

    if not subsequence or subsequence[-1] != nums[index]:
        # Don't pick
        findSubset(index + 1, subsequence, ans, nums)


def subsetsWithDup(nums):
    ans = []
    nums.sort()
    findSubset(0, [], ans, nums)
    return ans


nums = [0, 1, 2]
print(subsetsWithDup(nums))
