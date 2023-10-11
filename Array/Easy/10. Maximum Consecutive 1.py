def findMaxConsecutiveOnes(nums):
    n = len(nums)

    max_consecutive_ones = 0
    curr_consecutive_ones = 0

    for i in range(n):
        if nums[i]:
            curr_consecutive_ones += 1
            max_consecutive_ones = max(curr_consecutive_ones, max_consecutive_ones)
        else:
            curr_consecutive_ones = 0

    return max_consecutive_ones


nums = [1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(nums))
