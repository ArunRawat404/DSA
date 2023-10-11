# Approach 1


# def missingNumber(nums):
#     n = len(nums)

#     # Sum of first n natural numbers - Sum of all elements in nums will be missing number
#     total_sum = (n * (n + 1)) // 2
#     nums_sum = 0

#     for i in range(n):
#         nums_sum += nums[i]

#     return total_sum - nums_sum


# Approach 2
def missingNumber(nums):
    N = len(nums)
    xor1 = 0
    xor2 = 0

    for i in range(N):
        xor1 = xor1 ^ (i + 1)  # XOR up to [1...N-1]

    for i in range(N - 1):
        xor2 = xor2 ^ nums[i]  # XOR of array elements

    xor1 = xor1 ^ N  # XOR up to [1...N]

    return xor1 ^ xor2  # the missing number


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(nums))
