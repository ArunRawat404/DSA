def breakPossible(i, j, s, word_hashmap, sentence, ans):
    for j in range(i, len(s)):

        # checking if word exist in dictionary
        if s[i : j + 1] in word_hashmap:
            if len(sentence):
                sentence += " " + s[i : j + 1]
            else:
                sentence += s[i : j + 1]
            # if word exist in dictionary and it reached end of string means word can be broken
            if j == len(s) - 1:
                ans.append(sentence)
                return

            # recursion to check further string can be broken
            breakPossible(j + 1, j + 1, s, word_hashmap, sentence, ans)
            # removing the last word inserted(including empty space)
            sentence = sentence[: -(len(s[i : j + 1])) - 1]


def wordBreak(s, wordDict):
    word_hashmap = {}

    for word in wordDict:
        word_hashmap[word] = 1

    ans = []
    breakPossible(0, 0, s, word_hashmap, "", ans)

    if len(ans) == 0:
        return [-1]
    return ans


s = "godisnowherenowhere"
wordDict = ["god", "is", "now", "no", "where", "here"]
print(wordBreak(s, wordDict))


# recursion will give time limit exceeded, can be done using dynamic programming


# def breakPossible(i, j, s, word_hashmap):
#     for j in range(i, len(s)):
#         # checking if word exist in dictionary
#         if s[i : j + 1] in word_hashmap:
#             # if word exist in dictionary and it reached end of string means word can be broken
#             if j == len(s) - 1:
#                 return True

#             # recursion to check further string can be broken
#             if breakPossible(j + 1, j + 1, s, word_hashmap):
#                 return True
#     return False


# def wordBreak(s, wordDict):
#     word_hashmap = {}

#     for word in wordDict:
#         word_hashmap[word] = 1

#     return breakPossible(0, 0, s, word_hashmap)


# s = "leetcode"
# wordDict = ["leet", "code"]
# print(wordBreak(s, wordDict))


# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# wordDict = [
#     "a",
#     "aa",
#     "aaa",
#     "aaaa",
#     "aaaaa",
#     "aaaaaa",
#     "aaaaaaa",
#     "aaaaaaaa",
#     "aaaaaaaaa",
#     "aaaaaaaaaa",
# ]
