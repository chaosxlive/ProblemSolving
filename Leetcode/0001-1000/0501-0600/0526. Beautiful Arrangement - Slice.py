# https://leetcode.com/problems/beautiful-arrangement/

from functools import lru_cache
from typing import Tuple


class Solution:

    def countArrangement(self, n: int) -> int:

        @lru_cache(None)
        def solve(unuseds: Tuple[int]):
            if len(unuseds) == 0:
                return 1
            i = n - len(unuseds) + 1
            result = 0
            for j, num in enumerate(unuseds):
                if i % num > 0 and num % i > 0:
                    continue
                result += solve(tuple(unuseds[:j] + unuseds[j + 1:]))
            return result

        return solve(tuple(i for i in range(1, n + 1)))
