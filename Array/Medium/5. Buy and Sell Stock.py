def maxProfit(prices):
    max_profit = 0
    minimum = 0

    for i in range(1, len(prices)):
        if prices[i] < prices[minimum]:
            minimum = i

        profit = prices[i] - prices[minimum]
        if profit > max_profit:
            max_profit = profit

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
