def calSubsetSum(index, total, ans, nums):
    if index >= len(nums):
        ans.append(total)
        return

    # element is picked
    calSubsetSum(index + 1, total + nums[index], ans, nums)

    # element is not picked
    calSubsetSum(index + 1, total, ans, nums)


def subsetSum(nums):
    ans = []
    calSubsetSum(0, 0, ans, nums)
    ans.sort()
    return ans


nums = [4, 5]
print(subsetSum(nums))
