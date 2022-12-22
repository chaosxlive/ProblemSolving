# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) == 1:
            return 0
        state = [
            0,
            -prices[0]
        ]  # 0: Can buy, 1: Can sell
        for day in range(1, len(prices)):
            price = prices[day]
            state = [
                max(state[0], price + state[1] - fee),
                max(state[1], state[0] - price)
            ]
        return max(state)
