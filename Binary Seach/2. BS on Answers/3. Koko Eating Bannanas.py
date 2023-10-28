import math


def findMax(piles):
    maximum = 0
    for pile in piles:
        if pile > maximum:
            maximum = pile

    return maximum


def EatingTimeCalculator(eating_speed, piles):
    time_taken = 0
    for pile in piles:
        time_taken += math.ceil(pile / eating_speed)

    return time_taken


def minEatingSpeed(piles, h):
    start = 1
    end = findMax(piles)

    while start <= end:
        mid = start + (end - start) // 2
        time_taken = EatingTimeCalculator(mid, piles)
        if time_taken <= h:
            end = mid - 1
        else:
            start = mid + 1

    return start


piles = [10]
h = 9
print(minEatingSpeed(piles, h))
