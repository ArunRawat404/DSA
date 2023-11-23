def countDistinctSubsequences(index, string, subsequence, res):
    if index >= len(string):
        if len(subsequence) != 0:
            # adding distinct subsequence in set
            res.add(subsequence)
        return

    # take or pick particular index into the sequence
    subsequence += string[index]
    countDistinctSubsequences(index + 1, string, subsequence, res)

    # not pick, or not take condition, this element is not added to your subsequence
    subsequence = subsequence[:-1]
    countDistinctSubsequences(index + 1, string, subsequence, res)


def moreSubsequence(a, b):

    # using set to keep unique subsequences
    distinct_subarray_a = set()
    distinct_subarray_b = set()

    countDistinctSubsequences(0, a, "", distinct_subarray_a)
    countDistinctSubsequences(0, b, "", distinct_subarray_b)

    if len(distinct_subarray_a) >= len(distinct_subarray_b):
        return a
    else:
        return b


a = "abc"
b = "aaa"
print(moreSubsequence(a, b))
