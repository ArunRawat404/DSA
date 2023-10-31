def findKthPositive(arr, k):
    start = 0
    end = len(arr) - 1

    # Two edge cases that should improve running time
    if k < arr[start]:
        return k
    if k > arr[end] - len(arr):
        return k + len(arr)

    while start <= end:
        mid = start + (end - start) // 2

        missing_num = arr[mid] - (mid + 1)
        if missing_num < k:
            start = mid + 1
        else:
            end = mid - 1

    return end + k + 1


arr = [4, 7, 9, 10]
k = 7
print(findKthPositive(arr, k))
