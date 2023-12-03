# https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        covered = 0
        for coin in sorted(coins):
            if coin > covered + 1:
                break
            covered += coin
        return covered + 1
