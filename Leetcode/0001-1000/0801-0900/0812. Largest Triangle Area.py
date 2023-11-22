# https://leetcode.com/problems/largest-triangle-area/

class Solution:
    def largestTriangleArea(self, points) -> float:
        result = 0
        for p1 in range(len(points) - 2):
            x1, y1 = points[p1]
            for p2 in range(p1 + 1, len(points) - 1):
                x2, y2 = points[p2]
                for p3 in range(p2 + 1, len(points)):
                    x3, y3 = points[p3]
                    result = max(result, abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))))
        return result
