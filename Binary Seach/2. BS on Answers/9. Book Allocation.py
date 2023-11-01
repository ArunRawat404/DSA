def countStudents(arr, pages):
    pages_student = 0
    students = 1
    for i in range(len(arr)):
        if pages_student + arr[i] <= pages:
            # add pages to current student
            pages_student += arr[i]
        else:
            # add pages to next student
            pages_student = arr[i]
            students += 1

    return students


def findPages(arr, m):
    # we cannot allocate books as each student need atleast one book
    if m > len(arr):
        return -1

    start = max(arr)
    end = sum(arr)

    while start <= end:
        mid = start + (end - start) // 2
        students = countStudents(arr, mid)
        if students <= m:
            end = mid - 1
        else:
            start = mid + 1

    return start


arr = [12, 34, 67, 90]
m = 2
print(findPages(arr, m))
