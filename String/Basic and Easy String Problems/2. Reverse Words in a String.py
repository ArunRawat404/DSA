def reverseWords(s):
    res = ""
    word = ""
    #  + " " for adding last word
    for char in s + " ":
        if char != " ":
            word += char
        elif word:
            res = word + " " + res
            word = ""

    # trimming last " "
    return res[:-1]


s = "the sky is blue"
print(reverseWords(s))
