def largestOddNumber(num):
    last_odd_index = -1

    # traversing from back of string to starting of string
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 == 1:
            last_odd_index = i
            break

    if last_odd_index == -1:
        return ""
    return num[: last_odd_index + 1]


num = "35427"
print(largestOddNumber(num))
