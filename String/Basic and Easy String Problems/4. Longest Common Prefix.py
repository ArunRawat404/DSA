def longestCommonPrefix(strs):
    if not strs:
        return -1

    # retrieving min max by alphabetical order
    s1 = min(strs)
    s2 = max(strs)

    for index, char in enumerate(s1):
        if char != s2[index]:
            print("hi")
            if s1[:index] == "":
                return -1
            return s1[:index]

    print("hi2")
    if s1 == "":
        return -1
    return s1


strs = ["abcd", "Abcd", "abc"]
print(longestCommonPrefix(strs))


# def longestCommonPrefix(strs):
#     if not strs:
#         return ""

#     # retrieving min max by alphabetical order
#     s1 = min(strs)
#     s2 = max(strs)

#     for index, char in enumerate(s1):
#         if char != s2[index]:
#             return s1[:index]

#     return s1
