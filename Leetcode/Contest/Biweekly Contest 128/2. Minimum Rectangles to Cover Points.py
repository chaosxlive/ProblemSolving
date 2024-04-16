from typing import List, Optional


class Solution:

    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        res = 0
        target = -1
        for px, py in points:
            if px > target:
                res += 1
                target = px + w
        return res


# print(Solution().)
