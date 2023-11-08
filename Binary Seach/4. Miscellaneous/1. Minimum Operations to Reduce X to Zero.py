def minOperations(nums, x):
    n = len(nums)
    start = 0
    end = n - 1
    total = sum(nums)

    mid = start + (end - start) // 2
    min_ans = float("inf")
    temp_total = total - nums[mid]
    left = mid - 1
    right = mid + 1

    while left >= 0 and right <= n - 1:
        if nums[left] > nums[right]:
            temp_total -= nums[left]
            if temp_total == x:
                left += 1
                min_ans = min(min_ans, end - right + left + 1)
        else:
            temp_total -= nums[right]

        print(min_ans, temp_total)
        left -= 1
        right += 1


nums = [1, 1, 4, 2, 3]
x = 5
print(minOperations(nums, x))
