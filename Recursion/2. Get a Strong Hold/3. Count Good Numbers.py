def countGoodNumbers(n):
    ans = 1
    rem = n % 2
    n -= rem
    mod = 10**9 + 7
    # (first argument ** second argument) % third argument
    ans = pow(20, n // 2, mod)
    # if n is odd ans will be ans * 5
    if rem == 1:
        ans *= 5
    return ans % mod


n = 641263
print(countGoodNumbers(n))
