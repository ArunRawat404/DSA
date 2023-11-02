def countPainters(boards, time):
    painters = 1
    boards_painter = 0
    for i in range(len(boards)):
        if boards_painter + boards[i] <= time:
            # allocate board to current painter
            boards_painter += boards[i]
        else:
            # allocate board to next painter
            painters += 1
            boards_painter = boards[i]

    return painters


def findLargestMinDistance(boards, k):
    start = max(boards)
    end = sum(boards)

    while start <= end:
        mid = start + (end - start) // 2
        painters = countPainters(boards, mid)
        if painters <= k:
            end = mid - 1
        else:
            start = mid + 1

    return start


boards = [10, 20, 30, 40]
k = 2
print(findLargestMinDistance(boards, k))
