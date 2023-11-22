# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxBefore, maxAfter = [0] * len(prices), [0] * len(prices)
        currentMin = prices[0]
        for index in range(1, len(prices)):
            maxBefore[index] = max(maxBefore[index - 1], prices[index] - currentMin)
            currentMin = min(currentMin, prices[index])
        currentMax = prices[-1]
        for index in range(len(prices) - 2, -1, -1):
            maxAfter[index] = max(maxAfter[index + 1], currentMax - prices[index])
            currentMax = max(currentMax, prices[index])

        result = 0
        for day in range(len(prices)):
            result = max(result, maxBefore[day] + maxAfter[day])
        return result
