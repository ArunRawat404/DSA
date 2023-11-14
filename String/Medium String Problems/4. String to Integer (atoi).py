def myAtoi(s):
    positive = 1
    value = 0
    symbols = {"-": -1, "+": 1}
    left = 0

    # processing whitespaces " "
    while left < len(s) and s[left] == " ":
        left += 1

    # processing "+" or "-" sign
    if left < len(s) and s[left] in symbols:
        positive = symbols[s[left]]
        left += 1

    # processing the number
    while left < len(s) and s[left].isdigit():
        value = (value * 10) + int(s[left])
        left += 1

    # bound check
    ans = value * positive
    if ans >= 2**31 - 1:
        return 2**31 - 1
    elif ans <= -(2**31):
        return -(2**31)

    return ans


s = ""
print(myAtoi(s))
