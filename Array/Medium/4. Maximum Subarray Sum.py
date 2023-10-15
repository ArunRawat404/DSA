def maxSubArray(nums):

    max_sum = nums[0]
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        max_sum = max(current_sum, max_sum)

        if current_sum < 0:
            current_sum = 0

    return max_sum


nums = [-2, -1, 1, -2]
print(maxSubArray(nums))
