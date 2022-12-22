# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            return 0 if prices[1] <= prices[0] else prices[1] - prices[0]
        state = [
            0,
            max(-prices[0], -prices[1]),
            prices[1] - prices[0]
        ]  # 0: Can buy, 1: Can sell, 2: Cooldown
        for day in range(2, len(prices)):
            price = prices[day]
            state = [
                max(state[0], state[2]),
                max(state[0] - price, state[1]),
                price + state[1]
            ]
        return max(state)
