def singleNumber(nums):

    """
    XOR of a ^ a = 0
    XOR of b ^ 0 = b
    So when we XOR all the elements of array nums all the pairs will result in 0 and XOR of 0 with number which appear once is number itself.
    """

    ans = 0
    for i in range(len(nums)):
        ans = ans ^ nums[i]

    return ans


nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))
