def isPossible(beginWord, endWord, wordDict, num_words):
    for char in "abcdefghijklmnopqrstuvwxyz":
        pass


def ladderLength(beginWord, endWord, wordList):
    wordDict = {}
    for word in wordList:
        wordDict[word] = 1

    num_words = 0

    if endWord not in wordDict:
        return num_words
    isPossible(beginWord, endWord, wordDict, num_words, num_words)


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
ladderLength(beginWord, endWord, wordList)
