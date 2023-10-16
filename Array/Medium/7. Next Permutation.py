def reverse(arr, starting, ending):
    while starting < ending:
        arr[starting], arr[ending] = arr[ending], arr[starting]
        starting += 1
        ending -= 1


def nextPermutation(nums):

    n = len(nums)

    # finding break point
    break_index = -1
    for i in range(n - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            break_index = i - 1
            break

    # if no break point found(array is in descending order, and it's next permutation will be it's reverse)
    if break_index == -1:
        reverse(nums, 0, n - 1)
        return

    # Find the next greater element and swap it with arr[break_index]:
    for i in range(n - 1, break_index, -1):
        if nums[i] > nums[break_index]:
            nums[i], nums[break_index] = nums[break_index], nums[i]
            reverse(nums, break_index + 1, n - 1)
            return


nums = [2, 6, 5, 15, 11, 8, 5]
nextPermutation(nums)
print(nums)
