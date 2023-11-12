def isAnagram(s, t):
    if len(s) != len(t):
        return False

    for char in "abcdefghijklmnopqrstuvwxzy":
        if s.count(char) != t.count(char):
            return False

    return True


s = "aacc"
t = "ccac"
print(isAnagram(s, t))
