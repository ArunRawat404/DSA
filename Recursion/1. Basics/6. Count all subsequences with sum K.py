# return array of all subsequences with sum k
def subarraysWithSumK(index, subsequence, total, k, ans):
    if index == len(array):
        # condition is satisfied
        if total == k:
            ans.append(subsequence.copy())
        return

    # take or pick particular index into the sequence
    subsequence.append(array[index])
    total += array[index]
    subarraysWithSumK(index + 1, subsequence, total, k, ans)

    # not pick, or not take condition, this element is not added to your subsequence
    total -= array[index]
    subsequence.pop()
    subarraysWithSumK(index + 1, subsequence, total, k, ans)


array = [1, 2, 3, 4, 5]
ans = []
k = 6
subarraysWithSumK(0, [], 0, k, ans)
print(ans)


# print any one subsequences with sum k
def subarrayWithSumK(index, subsequence, total, k):
    if index == len(array):
        # condition is satisfied
        if total == k:
            print(subsequence)
            return True
        return False

    # take or pick particular index into the sequence
    subsequence.append(array[index])
    total += array[index]
    if subarrayWithSumK(index + 1, subsequence, total, k):
        return True

    # not pick, or not take condition, this element is not added to your subsequence
    total -= array[index]
    subsequence.pop()
    if subarrayWithSumK(index + 1, subsequence, total, k):
        return True


array = [1, 2, 3, 4, 5]
k = 6
subarrayWithSumK(0, [], 0, k)

# count number of subsequence with sum k
def countSubarraysWithSumK(index, total, k):
    if index == len(array):
        # condition is satisfied
        if total == k:
            return 1
        return 0

    # take or pick particular index into the sequence
    total += array[index]
    left = countSubarraysWithSumK(index + 1, total, k)

    # not pick, or not take condition, this element is not added to your subsequence
    total -= array[index]
    right = countSubarraysWithSumK(index + 1, total, k)

    return left + right


array = [1, 2, 3, 4, 5]
k = 6
print(countSubarraysWithSumK(0, 0, k))
