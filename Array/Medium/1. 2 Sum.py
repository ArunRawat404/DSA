# Approach 1 - Dictionary


def twoSum(nums, target):
    n = len(nums)

    dict = {}

    for i in range(n):
        second_element = target - nums[i]

        if second_element in dict:
            print(dict)
            return [dict[second_element], i]

        else:
            dict[nums[i]] = i


# Approach 2 - Two pointer after sorting


# def twoSum(nums, target):
# nums.sort()

# n = len(nums)

# left = 0
# right = n - 1

# while left < right:
#     if nums[left] + nums[right] < target:
#         left += 1
#     elif nums[left] + nums[right] > target:
#         right -= 1
#     # if they are equal to target
#     else:
#         # returning the elements not index as due to sorting the indexes order has been changed
#         return [nums[left], nums[right]]


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
