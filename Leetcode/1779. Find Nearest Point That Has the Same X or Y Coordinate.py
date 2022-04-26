# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = -1
        dist = 100000

        def getManhattanDistance(x1, y1, x2, y2):
            return abs(x2 - x1) + abs(y2 - y1)

        for i, (px, py) in enumerate(points):
            if px == x or py == y:
                tempDist = getManhattanDistance(x, y, px, py)
                if tempDist < dist:
                    result = i
                    dist = tempDist
                elif tempDist == dist and i < result:
                    result = i
        return result
