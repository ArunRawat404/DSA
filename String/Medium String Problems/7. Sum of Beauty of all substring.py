def beautySum(s):
    beauty_total = 0

    # traversing through each substring
    for left in range(len(s)):
        freq_dict = {}

        for right in range(left, len(s)):
            if s[right] in freq_dict:
                freq_dict[s[right]] += 1
            else:
                freq_dict[s[right]] = 1

            # finding max and min freq
            max_freq = max(freq_dict.values())
            min_freq = min(freq_dict.values())

            beauty_total += max_freq - min_freq

    return beauty_total


s = "aabcbaa"
print(beautySum(s))
