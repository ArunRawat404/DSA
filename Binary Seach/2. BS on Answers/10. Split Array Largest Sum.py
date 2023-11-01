def countPartitions(nums, max_sum):
    partitions = 1
    subarray_sum = 0
    for i in range(len(nums)):
        if subarray_sum + nums[i] <= max_sum:
            # insert element to current subarray
            subarray_sum += nums[i]
        else:
            # insert element to next subarray
            partitions += 1
            subarray_sum = nums[i]

    return partitions


def splitArray(nums, k):
    start = max(nums)
    end = sum(nums)

    while start <= end:
        mid = start + (end - start) // 2

        partitions = countPartitions(nums, mid)
        if partitions <= k:
            end = mid - 1
        else:
            start = mid + 1

    return start


nums = [1, 2, 3, 4, 5]
k = 2
print(splitArray(nums, k))
