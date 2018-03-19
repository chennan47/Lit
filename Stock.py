# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.
#
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
#
# In this case, no transaction is done, i.e. max profit = 0.


#at most one transaction
def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


#as many transactions as you like
class Solution(object):
    def maxProfit(self, prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.


#at most two transactions
# O(n) time, O(n) space
def maxProfit(self, prices):
    if not prices:
        return 0

    # forward traversal, profits record the max profit
    # by the ith day, this is the first transaction
    profits = []
    max_profit = 0
    current_min = prices[0]
    for price in prices:
        current_min = min(current_min, price)
        max_profit = max(max_profit, price - current_min)
        profits.append(max_profit)

    # backward traversal, max_profit records the max profit
    # after the ith day, this is the second transaction
    total_max = 0
    max_profit = 0
    current_max = prices[-1]
    for i in range(len(prices) - 1, -1, -1):
        current_max = max(current_max, prices[i])
        max_profit = max(max_profit, current_max - prices[i])
        total_max = max(total_max, max_profit + profits[i])

    return total_max


# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions.


#at most K transaction
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        if k >= len(prices) // 2:
            return sum(x - y for x, y in zip(prices[1:], prices[:-1]) if x > y)

        profits = [0] * len(prices)
        for j in range(k):

            preprofit = 0
            for i in range(1, len(prices)):
                profit = prices[i] - prices[i - 1]
                preprofit = max(preprofit + profit, profits[i])
                profits[i] = max(profits[i - 1], preprofit)

        return profits[-1]
