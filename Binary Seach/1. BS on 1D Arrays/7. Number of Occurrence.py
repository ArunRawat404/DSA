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


def count(arr, x):
    first_occurrence = firstOccurrence(arr, x)
    last_occurrence = lastOccurrence(arr, x)
    # if target doesn't exist in array
    if first_occurrence == -1:
        return 0
    return last_occurrence - first_occurrence + 1


arr = [1, 2, 4, 4, 5]
x = 5
print(count(arr, x))
