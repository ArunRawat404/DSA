def generateParenthesis(left, right, parentheses, ans):
    if len(parentheses) == n * 2:
        ans.append(parentheses)
        return

    # maximum "(" in parentheses will be n
    if left < n:
        generateParenthesis(left + 1, right, parentheses + "(", ans)

    # only add ")" when extra "(" these are already present to make valid parentheses
    if right < left:
        generateParenthesis(left, right + 1, parentheses + ")", ans)


n = 2
ans = []
generateParenthesis(0, 0, "", ans)
print(ans)
