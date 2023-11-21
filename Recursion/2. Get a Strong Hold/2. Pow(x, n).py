def myPowRecursive(x, n):
    if not n:
        return 1
    # negative
    if n < 0:
        return 1 / myPowRecursive(x, -n)
    if n % 2:
        return x * myPowRecursive(x, n - 1)
    return myPowRecursive(x * x, n // 2)


# Iterative
def myPow(x, n):
    # negative power
    if n < 0:
        n = -n
        x = 1 / x

    ans = 1
    base = x
    while n > 0:
        if n % 2:
            ans = ans * base
            n -= 1
        else:
            n = n // 2
            base = base * base

    return ans


x = 2
n = -2
print(myPow(x, n))
print(myPowRecursive(x, n))
