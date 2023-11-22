# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

from typing import List
from functools import lru_cache


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        @lru_cache(None)
        def find(pileIdx: int, quota: int) -> int:
            if pileIdx == len(piles) or quota == 0:
                return 0

            result = find(pileIdx + 1, quota)
            pile = piles[pileIdx]
            pileSum = 0
            for i in range(min(len(pile), quota)):
                pileSum += pile[i]
                result = max(result, pileSum + find(pileIdx + 1, quota - i - 1))

            return result

        return find(0, k)
