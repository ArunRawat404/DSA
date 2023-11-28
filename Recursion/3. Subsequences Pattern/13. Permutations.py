# Better solution without hashmap
def findPermutationOpt(ans, nums, index):
    if index == len(nums):
        ans.append(nums.copy())
        return

    for i in range(index, len(nums)):
        # swapping to generate permutations
        nums[i], nums[index] = nums[index], nums[i]

        findPermutationOpt(ans, nums, index + 1)

        # backtrack
        nums[i], nums[index] = nums[index], nums[i]


def findPermutation(permutation, ans, nums, permute_dict):
    if len(permutation) == len(nums):
        ans.append(permutation.copy())
        return

    for i in range(len(nums)):
        if i not in permute_dict or permute_dict[i] != True:
            permutation.append(nums[i])
            permute_dict[i] = True
            findPermutation(permutation, ans, nums, permute_dict)
            permute_dict[i] = False
            permutation.pop()


def permute(nums):
    permute_dict = {}
    ans = []
    # findPermutation([], ans, nums, permute_dict)
    findPermutationOpt(ans, nums, 0)
    return ans


nums = [1, 2, 3]
print(permute(nums))
