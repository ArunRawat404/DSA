def findMinTotal(weights):
    maximum = float("-inf")
    total = 0
    for weight in weights:
        total += weight
        if weight >= maximum:
            maximum = weight

    return maximum, total


def minDays(weights, capacity):
    numberOfDays = 1
    load = 0

    for weight in weights:
        if load + weight > capacity:
            numberOfDays += 1  # move to next day
            load = weight  # load the weight
        else:
            # load the weight on the same day
            load += weight

    return numberOfDays


def shipWithinDays(weights, days):
    maximum, total = findMinTotal(weights)
    start = maximum
    end = total

    while start <= end:
        mid = start + (end - start) // 2

        numberOfDays = minDays(weights, mid)
        if numberOfDays <= days:
            # Eliminate right half
            end = mid - 1
        else:
            # Eliminate left half
            start = mid + 1

    return start


weights = [1, 2, 3, 1, 1]
days = 4
print(shipWithinDays(weights, days))
