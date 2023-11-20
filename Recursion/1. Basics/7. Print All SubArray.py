# return array of all subarray
# def generate_subarrays(start, ans):
#     if start > len(array):
#         return

#     for i in range(start, len(array)):
#         subarray = array[start : i + 1]
#         ans.append(subarray)
#         generate_subarrays(i + 1, ans)


def generate_subarraysIterative(ans):
    for i in range(len(array)):

        for j in range(i, len(array)):

            ans.append(array[i : j + 1])


array = [1, 2, 3]
ans = []
ans2 = []
# generate_subarrays(0, ans)
generate_subarraysIterative(ans2)
print(ans)
print(ans2)
