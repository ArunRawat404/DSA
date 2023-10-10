def check(nums):
    # Check for first and last element too using modulo operator(%)
    count = 0
    n = len(nums)

    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1

    if count > 1:
        return False
    return True


nums = [3, 2, 1, 4, 5]
print(check(nums))
