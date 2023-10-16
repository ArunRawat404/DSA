def longestConsecutive(nums):
    di = {}

    for num in nums:
        di[num] = 1

    longest_consecutive = 0
    for num in nums:
        # checking if it's smallest number in consecutive sequence or not
        if (num - 1) not in di:
            curr_longest = 1
            while (num + curr_longest) in di:
                curr_longest += 1
            longest_consecutive = max(longest_consecutive, curr_longest)

    return longest_consecutive


nums = [1, 2, 1, 2]
print(longestConsecutive(nums))
