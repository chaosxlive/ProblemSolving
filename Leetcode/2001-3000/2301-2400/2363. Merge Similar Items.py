# https://leetcode.com/problems/merge-similar-items/

from collections import defaultdict


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for v, c in items1:
            d[v] = c
        for v, c in items2:
            d[v] += c
        return sorted(d.items())
