def rotateString(s, goal):
    if len(s) != len(goal):
        return False

    if goal in s + s:
        return True
    return False


s = "abcde"
goal = "cdeab"
print(rotateString(s, goal))
