def count(s, k):
    if not s:
        return 0
    char_count = {}
    num = 0
    left = 0

    for i in range(len(s)):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
        while len(char_count) > k:
            print("hi")
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                char_count.pop(s[left])
            left += 1
        num += i - left + 1
        print(k, num)

    return num


def countSubStrings(s, k):
    return count(s, k) - count(s, k - 1)


s = "abcbaa"
k = 3
print(countSubStrings(s, k))
