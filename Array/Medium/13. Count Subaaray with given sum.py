def subarraySum(nums, k):
    prefix_sum_dict = {}
    curr_sum = 0
    count = 0

    # Setting 0 in the map
    prefix_sum_dict[0] = 1
    for i in range(len(nums)):
        # add current element to prefix sum
        curr_sum += nums[i]

        # calculate the sum of remaining part i.e. x - k:
        remaining_sum = curr_sum - k

        if remaining_sum in prefix_sum_dict:
            count += prefix_sum_dict[remaining_sum]

        # Update the count of prefix sum
        if curr_sum in prefix_sum_dict:
            prefix_sum_dict[curr_sum] += 1
        else:
            prefix_sum_dict[curr_sum] = 1

    return count


nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 0
print(subarraySum(nums, k))
