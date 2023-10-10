import sys


def getSecondOrderElements(n, a):
    largest_element = 0
    smallest_element = sys.maxsize

    for i in range(n):
        if a[i] > largest_element:
            largest_element = a[i]

        if a[i] < smallest_element:
            smallest_element = a[i]

    second_largest = 0
    second_smallest = sys.maxsize

    for i in range(n):
        if largest_element > a[i] > second_largest:
            second_largest = a[i]

        if smallest_element < a[i] < second_smallest:
            second_smallest = a[i]

    return [second_largest, second_smallest]


n = 5
a = [1, 2, 3, 4, 5]
print(getSecondOrderElements(n, a))
