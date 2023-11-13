def maxDepth(s):
    max_depth = 0
    curr_depth = 0

    for char in s:
        if char == "(":
            curr_depth += 1
        elif char == ")":
            curr_depth -= 1
        max_depth = max(curr_depth, max_depth)

    return max_depth


s = "(1)+((2))+(((3)))"
print(maxDepth(s))
