# https://leetcode.com/problems/minimum-levels-to-gain-more-points/

from typing import List


class Solution:

    def minimumLevels(self, possible: List[int]) -> int:
        S = sum(map(lambda x: 1 if x == 1 else -1, possible))
        HS = S // 2
        d = 0
        for i in range(len(possible) - 1):
            p = 1 if possible[i] == 1 else -1
            d += p
            if d > HS:
                return i + 1
        return -1
