def findMinMax(bloomDay):
    maximum = 0
    # positive infinity
    minimum = float("inf")
    for bloom in bloomDay:
        if bloom > maximum:
            maximum = bloom
        if bloom < minimum:
            minimum = bloom

    return minimum, maximum


def bloomingTimeCalculator(bloomDay, day, m, k):
    flower_count = 0
    bouquets_count = 0
    for bloom in bloomDay:
        if bloom <= day:
            flower_count += 1
        else:
            bouquets_count += flower_count // k
            flower_count = 0

    bouquets_count += flower_count // k

    return bouquets_count >= m


def minDays(bloomDay, m, k):
    # total flower needed are more than available one
    total_flower = m * k
    if total_flower > len(bloomDay):
        return -1

    minimum, maximum = findMinMax(bloomDay)
    start = minimum
    end = maximum

    while start <= end:
        mid = start + (end - start) // 2
        # if ans is possible
        if bloomingTimeCalculator(bloomDay, mid, m, k):
            end = mid - 1
        else:
            start = mid + 1

    return start


bloomDay = [1, 2, 1, 2, 7, 2, 2, 3, 1]
# bouquets
m = 2
# flowers in each bouquet
k = 3

print(minDays(bloomDay, m, k))
