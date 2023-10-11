# Max Consecutive Ones III


def findMaxConsecutiveOnes(nums, m):
    n = len(nums)

    left, right = 0, 0
    curr_flips = 0
    max_cons_ones = 0

    while right < n:
        if nums[right] == 0:
            print("flipping", max_cons_ones)
            nums[right] = -1
            curr_flips += 1
        while left <= right and curr_flips > m:
            print("hi", curr_flips)
            if nums[left] == -1:
                curr_flips -= 1
            left += 1

        max_cons_ones = max(max_cons_ones, right - left + 1)
        print(max_cons_ones, "max")
        right += 1

    print(nums)
    return max_cons_ones


nums = [0, 0, 0, 1]

# number of flips
m = 4
print(findMaxConsecutiveOnes(nums, m))
