# Time Complexity: O(4 ^ N) * N)
# Space Complexity: O(N)


def findOperators(index, expression, result, prev_num, s, target, ans):
    if index == len(s):
        if result == target:
            ans.append(expression)
        return

    for j in range(index, len(s)):
        # skip leading zeros
        if j > index and s[index] == "0":
            break

        num = int(s[index : j + 1])

        # first number, pick it without adding operator
        if index == 0:
            findOperators(
                j + 1, expression + str(num), result + num, num, s, target, ans
            )
        else:
            findOperators(
                j + 1, expression + "+" + str(num), result + num, num, s, target, ans
            )
            findOperators(
                j + 1, expression + "-" + str(num), result - num, -num, s, target, ans
            )
            #  multiply operator has a higher precedence than the addition and subtraction operators so we will keep track of the last operand in our expression and reverse it's effect on the expression's value while considering the multiply operator.
            findOperators(
                j + 1,
                expression + "*" + str(num),
                result - prev_num + prev_num * num,
                prev_num * num,
                s,
                target,
                ans,
            )


def addOperators(s, target):
    ans = []
    findOperators(0, "", 0, 0, s, target, ans)
    return ans


s = "123"
target = 15
print(addOperators(s, target))
