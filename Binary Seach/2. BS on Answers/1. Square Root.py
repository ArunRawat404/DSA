def floorSqrt(n):
    start = 1
    end = n
    ans = 0
    while start <= end:
        mid = start + (end - start) // 2
        value = mid * mid
        if value == n:
            ans = mid
            return ans
        elif value < n:
            # may be ans
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    return ans


n = 8
print(floorSqrt(n))
