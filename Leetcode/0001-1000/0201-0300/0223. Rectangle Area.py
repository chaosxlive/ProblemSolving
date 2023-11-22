# https://leetcode.com/problems/rectangle-area/

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        def calcArea(x1, y1, x2, y2):
            return (x2 - x1) * (y2 - y1)

        overlapX = max(min(ax2, bx2) - max(ax1, bx1), 0)
        overlapY = max(min(ay2, by2) - max(ay1, by1), 0)
        return calcArea(ax1, ay1, ax2, ay2) + calcArea(bx1, by1, bx2, by2) - overlapX * overlapY
