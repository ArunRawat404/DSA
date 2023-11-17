# sum of first n numbers using parameterized way
def summation(i, total):
    if i < 1:
        print(total)
        return

    summation(i - 1, total + i)


# sum of first n numbers using functional way
def summationFun(i):
    if i <= 1:
        return i

    return i + summationFun(i - 1)


# factorial of n using parameterized way
def factorial(i, fact):
    if i <= 1:
        print(fact)
        return

    factorial(i - 1, fact * i)


# factorial of n using functional way
def factorialFuc(i):
    if i <= 1:
        return 1

    return i * factorialFuc(i - 1)


n = 5
summation(n, 0)
print(summationFun(n))
factorial(n, 1)
print(factorialFuc(n))
