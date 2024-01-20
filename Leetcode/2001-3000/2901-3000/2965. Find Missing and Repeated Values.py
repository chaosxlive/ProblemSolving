# https://leetcode.com/problems/find-missing-and-repeated-values/

from typing import List


class Solution:

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ns = [c for r in grid for c in r]
        L = len(ns)
        total = sum(ns)
        s = set(ns)
        t = set(range(1, L + 1))
        miss = list(t - s)[0]
        return [total + miss - (1 + L) * L // 2, miss]
