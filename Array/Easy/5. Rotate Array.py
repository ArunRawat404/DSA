# left rotate array by 1


# def rotateArray(arr):
#     n = len(arr)
#     temp = arr[0]
#     for i in range(n - 1):
#         arr[i] = arr[i + 1]
#     arr[n - 1] = temp

#     return arr


# arr = [1, 2, 3, 4, 5]
# print(rotateArray(arr))


# rotate array to the right by k steps


def reverse(arr, left, right):
    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def rotateArray(arr, k):
    n = len(arr)

    # if k is greater than n
    k = k % n

    # reverse first n - k - 1 elements
    reverse(arr, 0, n - k - 1)

    # reverse last k elements
    reverse(arr, n - k, n - 1)

    # reverse whole array
    reverse(arr, 0, n - 1)


arr = [1, 2, 3, 4, 5]
k = 3
print(rotateArray(arr, k))
