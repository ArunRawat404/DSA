def search(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return True

        # when start, mid and end are same
        if nums[start] == nums[mid] == nums[end]:
            start += 1
            end -= 1
            continue

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
    return False


nums = [3, 4, 5, 0, 0, 1, 2]
target = 4
print(search(nums, target))
