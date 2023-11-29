# using hashmap
def findPermutationHashMap(nums, permutations, ans, count_dict):
    if len(permutations) == len(nums):
        ans.append(permutations.copy())
        return

    for num in count_dict:
        if count_dict[num] > 0:
            permutations.append(num)
            count_dict[num] -= 1

            findPermutationHashMap(nums, permutations, ans, count_dict)

            # backtrack
            permutations.pop()
            count_dict[num] += 1


def permuteUnique2(nums):
    # to create hash map from a array
    # import collections
    # counter = collections.Counter(nums)

    # creating a hashmap with value 0 for each num
    count_dict = {num: 0 for num in nums}
    for num in nums:
        count_dict[num] += 1

    ans = []
    findPermutationHashMap(nums, [], ans, count_dict)
    return ans


nums = [0, 2, 3, 2, 4]
print(permuteUnique2(nums))
