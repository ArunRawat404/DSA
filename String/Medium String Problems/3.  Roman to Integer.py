def romanToInt(s):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    ans = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman_dict[s[i]] < roman_dict[s[i + 1]]:
            ans -= roman_dict[s[i]]
        else:
            ans += roman_dict[s[i]]

    return ans


# another solution
# def romanToInt(s):
#     roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     ans = 0
#     s = s.replace("IV", "IIII").replace("IX", "VIIII")
#     s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#     s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#     for char in s:
#         ans += roman_dict[char]
#     return ans


s = "LVIII"
print(romanToInt(s))
