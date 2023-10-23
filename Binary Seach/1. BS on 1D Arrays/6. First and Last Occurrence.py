def firstOccurrence(nums, target):
    first_occurrence = -1

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == target:
            first_occurrence = mid
            end = mid - 1

        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return first_occurrence


def lastOccurrence(nums, target):
    last_occurrence = -1

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == target:
            last_occurrence = mid
            start = mid + 1

        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return last_occurrence


def searchRange(nums, target):
    if len(nums) == 0:
        return [-1, -1]

    first_occurrence = firstOccurrence(nums, target)
    last_occurrence = lastOccurrence(nums, target)
    return [first_occurrence, last_occurrence]


nums = [5, 7, 8, 8, 8, 10]
target = 8
print(searchRange(nums, target))
