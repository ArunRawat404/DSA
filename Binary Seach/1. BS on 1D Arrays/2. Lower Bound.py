def lowerBound(arr, x):
    start = 0
    end = len(arr) - 1

    ans = len(arr)

    while start <= end:
        mid = (start + end) // 2

        if x <= arr[mid]:
            ans = mid

            # look for smaller index on the left
            end = mid - 1

        else:
            # look on the right
            start = mid + 1

    return ans


arr = [1, 2, 2, 3]
x = 0
print(lowerBound(arr, x))
