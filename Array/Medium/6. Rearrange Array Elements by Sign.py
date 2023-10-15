def rearrangeArray(nums):
    ans_arr = [0] * len(nums)
    positive_pos = 0
    negative_pos = 1

    for element in nums:
        if element > 0:
            ans_arr[positive_pos] = element
            positive_pos += 2
        else:
            ans_arr[negative_pos] = element
            negative_pos += 2

    return ans_arr


nums = [3, 1, -2, -5, 2, -4]
print(rearrangeArray(nums))
