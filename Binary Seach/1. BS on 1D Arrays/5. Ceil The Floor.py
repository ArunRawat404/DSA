# Ceil of x is the smallest element in array which is greater than or equal to x
def findCeil(arr, x):
    ceil = -1

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if x <= arr[mid]:
            ceil = arr[mid]
            end = mid - 1

        else:
            start = mid + 1

    return ceil


# Floor of x is the largest element in array which is smaller than or equal to x
def findFloor(arr, x):
    floor = -1

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if x >= arr[mid]:
            floor = arr[mid]
            start = mid + 1

        else:
            end = mid - 1

    return floor


def ceilingInSortedArray(arr, x):
    arr.sort()
    ceil = findCeil(arr, x)
    floor = findFloor(arr, x)
    return floor, ceil


arr = [4, 3, 8, 4, 7, 10]
x = 5
print(ceilingInSortedArray(arr, x))
