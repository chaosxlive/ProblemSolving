# https://leetcode.com/problems/stone-game-ii/

from typing import List
from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        @lru_cache(None)
        def dfs(idx, M, isAlice):
            if idx >= len(piles):
                return 0
            result = 0 if isAlice else 2147483647
            for X in range(1, min(M*2, len(piles) - idx)+1):
                if isAlice:
                    result = max(result, sum(piles[idx:idx + X]) + dfs(idx + X, max(M, X), False))
                else:
                    result = min(result, dfs(idx + X, max(M, X), True))
            return result

        return dfs(0, 1, True)
