def moveZeroes(nums):
    zero_pos = -1
    # getting first zero position
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_pos = i
            break

    # if no zeroes are present
    if zero_pos == -1:
        return nums

    # swapping non-zero elements with zeroes position
    for i in range(zero_pos + 1, len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
            zero_pos += 1

    return nums


nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))
