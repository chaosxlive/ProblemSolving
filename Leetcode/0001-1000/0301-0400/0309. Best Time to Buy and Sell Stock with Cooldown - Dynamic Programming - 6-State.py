# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        state = (
            0,  # notKeepSkipProfit
            0,  # keepSkipProfit
            -1,  # keepSkipValue
            0,  # buyProfit
            -1,  # buyValue
            0   # sellProfit
        )
        for price in prices:
            state = (
                max(state[0], state[5]),
                0 if state[2] == -1 and state[4] == -1 else (state[3] if state[2] == -1 else (state[1] if state[1] > state[3] else ((state[1] if state[2] < state[4] else state[3]) if state[1] == state[3] else state[3]))),
                -1 if state[2] == -1 and state[4] == -1 else (state[4] if state[2] == -1 else (state[2] if state[1] > state[3] else ((state[2] if state[2] < state[4] else state[4]) if state[1] == state[3] else state[4]))),
                state[0] - price,
                price,
                0 if state[4] == -1 else ((state[3] + price) if state[2] == -1 else (max(state[1], state[3]) + price))
            )
        return max(state[0], state[1], state[3], state[5])
