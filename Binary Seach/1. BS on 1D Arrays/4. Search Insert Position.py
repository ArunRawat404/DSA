def searchInsert(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] < target:
            start = mid + 1
        else:
            if nums[mid] == target and nums[mid - 1] != target:
                return mid
            else:
                end = mid - 1

    return start


nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))
