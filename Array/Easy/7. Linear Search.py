def linearSearch(num, arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == num:
            return i

    return -1


arr = [6, 7, 8, 4, 1]
num = 4
print(linearSearch(num, arr))
