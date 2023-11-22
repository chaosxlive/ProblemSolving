# https://leetcode.com/problems/check-distances-between-same-letters/

from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        seen = {}
        for i, c in enumerate(s):
            if c not in seen:
                seen[c] = i
            elif i - seen[c] - 1 != distance[ord(c) - 97]:
                return False
        return True
