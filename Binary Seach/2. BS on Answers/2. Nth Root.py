# power exponential method -> O(log2N)
def func(i, exp):
    ans = 1
    base = i

    while exp > 0:
        if exp % 2:
            exp -= 1
            ans = base * ans
        else:
            exp //= 2
            base = base * base

    return ans


def NthRoot(n, m):
    start = 1
    end = m

    while start <= end:
        mid = start + (end - start) // 2
        value = func(mid, n)
        if value == m:
            return mid
        elif value < m:
            start = mid + 1
        else:
            end = mid - 1

    return -1


n = 5
m = 32768
print(NthRoot(n, m))
