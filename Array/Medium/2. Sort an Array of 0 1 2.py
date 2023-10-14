def sortColors(nums):
    # Approach - Two pointer with a current value
    current = 0
    zero_pos = 0
    two_pos = len(nums) - 1

    while current <= two_pos:
        if nums[current] == 0:
            nums[current], nums[zero_pos] = nums[zero_pos], nums[current]
            current += 1
            zero_pos += 1

        elif nums[current] == 1:
            current += 1
        else:
            nums[current], nums[two_pos] = nums[two_pos], nums[current]
            two_pos -= 1


nums = [0, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 0]
sortColors(nums)
print(nums)
