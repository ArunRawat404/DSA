def majorityElement(nums):
    n = len(nums)
    cnt1, cnt2 = 0, 0
    element1, element2 = None, None

    for i in range(n):
        if cnt1 == 0 and element2 != nums[i]:
            cnt1 = 1
            element1 = nums[i]
        elif cnt2 == 0 and element1 != nums[i]:
            cnt2 = 1
            element2 = nums[i]
        elif element1 == nums[i]:
            cnt1 += 1
        elif element2 == nums[i]:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    ans = []

    # Checking if the stored element is the majority elements

    check_count1 = 0
    check_count2 = 0

    for i in range(n):
        if nums[i] == element1:
            check_count1 += 1
        if nums[i] == element2:
            check_count2 += 1

    if check_count1 > (n / 3):
        ans.append(element1)

    if check_count2 > (n / 3):
        ans.append(element2)

    return ans


nums = [2, 2, 3, 2, 5, 1, 1, 1, 1]
print(majorityElement(nums))
