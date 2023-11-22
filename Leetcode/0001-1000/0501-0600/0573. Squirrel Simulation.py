# https://leetcode.com/problems/squirrel-simulation/

from typing import List


class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:

        def calcDist(aX, aY, bX, bY):
            return abs(aX - bX) + abs(aY - bY)

        totalDist = 0
        saved = -2147483648
        for (nutX, nutY) in nuts:
            treeDist = calcDist(tree[0], tree[1], nutX, nutY)
            squirrelDist = calcDist(squirrel[0], squirrel[1], nutX, nutY)
            totalDist += treeDist * 2
            saved = max(saved, treeDist - squirrelDist)
        return totalDist - saved
