def getLongestSubarray(nums, k):
    prefix_sum_dict = {}
    curr_sum = 0
    max_len = 0

    for i in range(len(nums)):
        # calculate the prefix sum till index i
        curr_sum += nums[i]

        # if the sum = k update max_len
        if curr_sum == k:
            max_len = max(max_len, i + 1)

        # calculate the sum of remaining part i.e. x - k:
        remaining_sum = curr_sum - k

        # if remaining part is a subarray with sum = k
        if remaining_sum in prefix_sum_dict:
            max_len = max(max_len, i - prefix_sum_dict[remaining_sum])

        # for making sure curr_sum is not updated in hash map
        if curr_sum not in prefix_sum_dict:
            prefix_sum_dict[curr_sum] = i

    return max_len


nums = [2, -2, 1, 2, 1, 0, 1, 1]
k = 4
print(getLongestSubarray(nums, k))
