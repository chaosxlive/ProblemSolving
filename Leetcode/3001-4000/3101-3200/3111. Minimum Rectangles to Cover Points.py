# https://leetcode.com/problems/minimum-rectangles-to-cover-points/

from typing import List


class Solution:

    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        res = 0
        target = -1
        for px, _ in points:
            if px > target:
                res += 1
                target = px + w
        return res
