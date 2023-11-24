# def subarraysWithSumK(a, k, start, end, ans):
#     if start > end:
#         return

#     for i in range(start, end):
#         subarray = a[start : i + 1]

#         ans.append(subarray)
#         subarraysWithSumK(a, k, i + 1, end, ans)


# a = [1, 2, 3]
# k = 3
# ans = []
# subarraysWithSumK(a, k, 0, len(a), ans)
# print(ans)
