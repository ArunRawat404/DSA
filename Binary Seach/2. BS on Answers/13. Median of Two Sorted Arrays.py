def findMedianSortedArrays(nums1, nums2):
    len1 = len(nums1)
    len2 = len(nums2)
    total_len = len1 + len2

    # performing binary search on smaller size array
    if len1 > len2:
        return findMedianSortedArrays(nums2, nums1)

    start = 0
    end = len1
    left = (len1 + len2 + 1) // 2
    while start <= end:
        mid1 = start + (end - start) // 2
        mid2 = left - mid1
        l1, l2 = float("-inf"), float("-inf")
        r1, r2 = float("inf"), float("inf")
        if mid1 < len1:
            r1 = nums1[mid1]
        if mid2 < len2:
            r2 = nums2[mid2]
        if mid1 - 1 >= 0:
            l1 = nums1[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = nums2[mid2 - 1]

        if l1 <= r2 and l2 <= r1:
            if total_len % 2 == 1:
                return max(l1, l2)
            else:
                return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0

        # eliminate the halves:
        elif l1 > r2:
            end = mid1 - 1
        else:
            start = mid1 + 1
    return 0  # dummy statement


nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))
