def isIsomorphic(s, t):
    dictS, dictT = {}, {}

    for i in range(len(s)):
        if (s[i] in dictS and dictS[s[i]] != t[i]) or (
            t[i] in dictT and dictT[t[i]] != s[i]
        ):
            return False

        dictS[s[i]] = t[i]
        dictT[t[i]] = s[i]

    return True


s = "zvsuu"
t = "qonoo"
print(isIsomorphic(s, t))
