def removeDuplicates(arr):
    n = len(arr)

    count = 0
    for i in range(1, n):
        if arr[count] != arr[i]:
            count += 1
            arr[count] = arr[i]

    return count + 1


arr = [1, 1, 2, 2, 2, 3]
print(removeDuplicates(arr))
