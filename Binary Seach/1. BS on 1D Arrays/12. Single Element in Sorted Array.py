def singleNonDuplicate(nums):
    start = 0
    end = len(nums) - 1

    # For Edge Cases
    if len(nums) == 1:
        # If only one element is in the array
        return nums[0]

    if nums[start] != nums[start + 1]:
        # If the first element is the element that appears only once
        return nums[start]

    if nums[end] != nums[end - 1]:
        # If Last element is the element that appears only once
        return nums[end]

    while start <= end:
        mid = start + (end - start) // 2
        # mid is single element
        if nums[mid - 1] != nums[mid] != nums[mid + 1]:
            return nums[mid]
        # We are in the left:
        elif (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (
            mid % 2 == 1 and nums[mid] == nums[mid - 1]
        ):
            # Eliminate the left half:
            start = mid + 1
        # We are in the right
        else:
            # Eliminate the right half:
            end = mid - 1

    return -1


nums = [3, 3, 7, 7, 10, 11, 11]
print(singleNonDuplicate(nums))
