def getKPermutation(n, k):
    factorial = 1
    numbers = []
    for i in range(1, n):
        factorial *= i
        numbers.append(i)

    # in above loop we are only going till n - 1
    numbers.append(n)

    ans = ""
    # for 0th based indexing
    k = k - 1

    while True:
        block_size = int(k / factorial)
        ans += str(numbers[block_size])
        # remove the number from array
        numbers.remove(numbers[block_size])
        if len(numbers) == 0:
            break

        # next value of k
        k = k % factorial
        # will give n - 1 factorial
        factorial = factorial / len(numbers)

    return ans


n = 4
k = 16
print(getKPermutation(n, k))
