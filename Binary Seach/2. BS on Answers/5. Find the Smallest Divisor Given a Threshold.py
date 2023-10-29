import math


def findMax(nums):
    maximum = 0
    for num in nums:
        if num > maximum:
            maximum = num

    return maximum


def calDivision(nums, div):
    total = 0
    # Find the summation of division values
    for num in nums:
        total += math.ceil(num / div)

    return total


def smallestDivisor(nums, threshold):
    start = 1
    end = findMax(nums)

    # answer not possible as it will exceed threshold
    if len(nums) > threshold:
        return -1

    while start <= end:
        mid = start + (end - start) // 2
        total = calDivision(nums, mid)
        if total <= threshold:
            end = mid - 1
        else:
            start = mid + 1

    return start


nums = [44, 22, 33, 11, 1]
threshold = 5
print(smallestDivisor(nums, threshold))
