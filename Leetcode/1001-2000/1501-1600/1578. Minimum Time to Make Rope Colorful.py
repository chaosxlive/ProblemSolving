# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        L = len(colors)
        total = neededTime[0]
        keep = 0
        prev = 0
        i = 1
        while i < L:
            if colors[i] != colors[prev]:
                keep += max(neededTime[prev:i])
                prev = i
            total += neededTime[i]
            i += 1
        keep += max(neededTime[prev:i])
        return total - keep
