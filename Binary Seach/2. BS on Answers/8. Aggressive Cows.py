def isPossible(stalls, k, distance):
    cnt_cows = 1
    last_pos_cow = 0
    for i in range(1, len(stalls)):
        if stalls[i] - stalls[last_pos_cow] >= distance:
            # place next cow
            cnt_cows += 1
            # update the last location
            last_pos_cow = i

        if cnt_cows >= k:
            return True

    return False


def aggressiveCows(stalls, k):
    n = len(stalls)
    stalls.sort()
    start = 1
    # maximum distance can be between furthest cows
    end = stalls[n - 1] - stalls[0]

    while start <= end:
        mid = start + (end - start) // 2

        if isPossible(stalls, k, mid):
            start = mid + 1
        else:
            end = mid - 1

    return end


stalls = [0, 3, 4, 7, 10, 9]
k = 4
print(aggressiveCows(stalls, k))
