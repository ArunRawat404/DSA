def findMin(nums):
    start = 0
    end = len(nums) - 1

    while start < end:
        mid = start + (end - start) // 2
        if nums[mid] >= nums[end]:
            start = mid + 1
        else:
            end = mid

    return start


nums = [3, 3, 1, 3]
print(findMin(nums))
