def isSubsetPresent(a, k, index):
    if k == 0:
        return True
    if k < 0:
        return False

    if index >= len(a):
        return False

    if isSubsetPresent(a, k - a[index], index + 1):
        return True

    if isSubsetPresent(a, k, index + 1):
        return True


a = [1, 2, 3]
k = 5
print(isSubsetPresent(a, k, 0))
