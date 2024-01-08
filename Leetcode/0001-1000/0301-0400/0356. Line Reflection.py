# https://leetcode.com/problems/line-reflection/

from collections import defaultdict
from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        horizonPoints = defaultdict(set)
        for x, y in points:
            horizonPoints[y].add(x)
        expectedX = None
        for pss in horizonPoints.values():
            ps = sorted(pss)
            for i in range(len(ps) // 2):
                x = (ps[i] + ps[-1 - i]) / 2
                if expectedX is None:
                    expectedX = x
                elif expectedX != x:
                    return False
            if len(ps) % 2 != 0:
                if expectedX is None:
                    expectedX = ps[0]
                elif ps[len(ps) // 2] != expectedX:
                    return False
        return True
