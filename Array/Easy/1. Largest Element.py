def largestElement(arr, n):

    largest_element = arr[0]

    for i in range(1, n):
        if arr[i] > largest_element:
            largest_element = arr[i]

    return largest_element


n = 5
arr = [1, 2, 3, 4, 5]
print(largestElement(arr, n))
