# https://leetcode.com/problems/palindrome-partitioning/

from typing import List
from functools import lru_cache


class Solution:
    @lru_cache
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        result = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                for p in self.partition(s[i:]):
                    result.append([s[:i]] + p)
        return result
