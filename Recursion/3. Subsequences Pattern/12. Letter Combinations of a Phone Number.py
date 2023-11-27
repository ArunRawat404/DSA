def findCombinations(i, curr_str, ans, digits, digit_mapping):
    if len(curr_str) == len(digits):
        ans.append(curr_str)
        return

    #  going through each char in digit_mapping
    for char in digit_mapping[digits[i]]:
        findCombinations(i + 1, curr_str + char, ans, digits, digit_mapping)


def letterCombinations(digits):
    digit_mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    ans = []
    # if digit string is non empty
    if digits:
        findCombinations(0, "", ans, digits, digit_mapping)

    return ans


digits = "92"
print(letterCombinations(digits))
