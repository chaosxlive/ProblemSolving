# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        currentMin = prices[0]
        prev = prices[0]
        tempProfit = 0
        for price in prices[1:]:
            if price > prev:
                tempProfit = max(tempProfit, price - currentMin)
            else:
                result += tempProfit
                tempProfit = 0
                currentMin = price
            prev = price
        return result + tempProfit
