# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        def solve(qx, qy, qr):
            result = 0
            for px, py in points:
                if (px - qx) ** 2 + (py - qy) ** 2 <= qr ** 2:
                    result += 1
            return result

        return [solve(*query) for query in queries]
