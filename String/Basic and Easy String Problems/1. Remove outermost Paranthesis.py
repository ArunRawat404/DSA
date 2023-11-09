def removeOuterParentheses(s):
    ans = ""
    opened = 0

    for char in s:
        if char == "(":
            if opened > 0:
                ans += char
            opened += 1
        if char == ")":
            if opened > 1:
                ans += char
            opened -= 1
    return ans


s = "(()())(())"
print(removeOuterParentheses(s))
