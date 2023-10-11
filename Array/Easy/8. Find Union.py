def findUnion(a, b):
    union_array = []

    n, m = len(a), len(b)
    i, j = 0, 0

    while i < n and j < m:
        # for skipping duplicates elements in array
        while (i != (n - 1)) and (a[i] == a[i + 1]):
            i += 1

        while (j != (m - 1)) and (b[j] == b[j + 1]):
            j += 1

        if a[i] < b[j]:
            union_array.append(a[i])
            i += 1
        elif a[i] > b[j]:
            union_array.append(b[j])
            j += 1
        # for checking if a[i] == b[j]
        else:
            union_array.append(a[i])
            i += 1
            j += 1

    while i < n:
        union_array.append(a[i])
        i += 1

    while j < m:
        union_array.append(b[j])
        j += 1

    return union_array


a = [1, 2, 3, 3]
b = [2, 2, 4]
print(findUnion(a, b))
