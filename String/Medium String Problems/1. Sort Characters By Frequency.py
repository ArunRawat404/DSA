def frequencySort(s):
    # frequency dictionary
    freq_dict = {}

    for char in s:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    # list of tuples with first element as frequency and second as frequency * character
    substring_list = []
    for key in freq_dict:
        if freq_dict[key] not in substring_list:
            substring_list.append((freq_dict[key], key * freq_dict[key]))
        else:
            substring_list.append(
                (freq_dict[key], substring_list[freq_dict[key]] + key)
            )
    # sort list in reverse order by frequency
    substring_list.sort(reverse=True)

    ans = ""
    for nested_list in substring_list:
        ans += nested_list[1]

    return ans


s = "Aabb"
print(frequencySort(s))
