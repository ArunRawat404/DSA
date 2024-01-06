# Memoization, top-down approach
# Time Complexity: O(N)
# Space Complexity: O(N) + O(N), stack space + dp array


def fib(n, dp):
    if n <= 1:
        return n
    # if sub problem is previously computed
    if dp[n] != -1:
        return dp[n]

    # store the answer of sub problem
    dp[n] = fib(n - 1, dp) + fib(n - 2, dp)

    return dp[n]


n = 10
dp = [-1 for _ in range(n + 1)]
print(fib(n, dp))


# tabulation, bottom-up approach
# Time Complexity: O(N)
# Space Complexity: O(N), dp array


def fibTab(n):
    dp = [-1 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(fibTab(n))


# Space optimization
# Time Complexity: O(N)
# Space Complexity: O(1)


def fibTabOpt(n):
    prev2 = 0
    prev = 1

    for i in range(2, n + 1):
        curr_i = prev + prev2

        prev2 = prev
        prev = curr_i

    return prev


print(fibTabOpt(n))
