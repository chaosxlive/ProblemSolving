# https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

from typing import List


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        result = 0
        coins.sort()
        curTotal = 0
        coinIdx = 0
        for n in range(1, target + 1):
            if curTotal < n:
                while coinIdx < len(coins) and coins[coinIdx] <= n:
                    curTotal += coins[coinIdx]
                    coinIdx += 1
                if curTotal < n:
                    result += 1
                    curTotal += n
        return result
