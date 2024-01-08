# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        return [sum(1 for px, py in points if (px - qx) ** 2 + (py - qy) ** 2 <= qr ** 2) for qx, qy, qr in queries]
