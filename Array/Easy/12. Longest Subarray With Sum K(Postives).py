def longestSubArrayWithSumK(a, k):

    left, right = 0, 0
    max_length = 0
    curr_sum = 0

    while right < len(a):
        curr_sum += a[right]

        # if curr_sum > k, reduce the subarray from left until sum becomes less or equal to k:
        while left <= right and curr_sum > k:
            curr_sum -= a[left]
            left += 1

        # if curr_sum = k, update the max_length
        if curr_sum == k:
            max_length = max(max_length, right - left + 1)
        right += 1

    return max_length


a = [1, 2, 3, 1, 1, 1, 1]
k = 3
print(longestSubArrayWithSumK(a, k))
