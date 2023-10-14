def majorityElement(nums):
    # Moore’s Voting Algorithm
    n = len(nums)
    count = 0
    element = None

    for i in range(n):
        if count == 0:
            count = 1
            element = nums[i]

        elif element == nums[i]:
            count += 1

        else:
            count -= 1

    # Checking if the stored element is the majority element

    count2 = 0

    for i in range(n):
        if nums[i] == element:
            count2 += 1

    if count2 > (n / 2):
        return element

    return -1


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))
