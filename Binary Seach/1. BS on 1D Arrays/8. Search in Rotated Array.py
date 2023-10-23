def search(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == target:
            return mid

        # left sorted portion
        if nums[start] <= nums[mid]:
            # right sorted portion
            if target < nums[start] or target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

        # right sorted portion
        else:
            # left sorted portion
            if target < nums[mid] or target > nums[end]:
                end = mid - 1
            else:
                start = mid + 1

    return -1


nums = [6, 1, 6]
target = 6
print(search(nums, target))
