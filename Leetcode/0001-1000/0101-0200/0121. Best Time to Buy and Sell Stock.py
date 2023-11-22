# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        currentMin = prices[0]
        for price in prices[1:]:
            if price > currentMin:
                result = max(result, price - currentMin)
            else:
                currentMin = min(currentMin, price)
        return result
