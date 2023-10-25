def findPeakElement(nums):
    if len(nums) == 1 or nums[0] > nums[1]:
        return 0

    n = len(nums)

    if nums[n - 1] > nums[n - 2]:
        return n - 1

    # 0th and n - 1 th index already checked
    start = 1
    end = n - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid

        # Find peak on the left
        elif nums[mid] < nums[mid - 1]:
            end = mid - 1

        # Find peak on the right
        else:
            start = mid + 1

    return -1


nums = [1, 2, 1, 3, 5, 6, 4]
print(findPeakElement(nums))
