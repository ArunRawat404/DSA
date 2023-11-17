# printing number from 1 to N
def print1ToN(i, n):
    if i > n:
        return
    print(i)
    print1ToN(i + 1, n)


# printing number from N to 1
def printNTo1(n):
    if n < 1:
        return
    print(n)
    printNTo1(n - 1)


# printing number from 1 to N using backtracking
def print1ToNBacktrack(n):
    if n < 1:
        return
    print1ToNBacktrack(n - 1)
    print(n)


# printing number from N to 1 using backtracking
def printNTo1Backtrack(i, n):
    if i > n:
        return
    printNTo1Backtrack(i + 1, n)
    print(i)


n = 5
# print1ToN(1, n)
# printNTo1(n)
# print1ToNBacktrack(n)
printNTo1Backtrack(1, n)
