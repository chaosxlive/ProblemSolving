# https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        currentX, currentY = points[0][0], points[0][1]

        for point in points:
            result += max(abs(point[0] - currentX), abs(point[1] - currentY))
            currentX, currentY = point[0], point[1]

        return result