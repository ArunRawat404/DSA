def superiorElements(nums):
    right = len(nums) - 1
    ans = []

    max_ele = 0

    while right >= 0:
        if nums[right] > max_ele:
            ans.append(nums[right])

        max_ele = max(max_ele, nums[right])

        right -= 1

    return ans


nums = [1, 2, 3, 2]
print(superiorElements(nums))
