# https://leetcode.com/problems/valid-boomerang/

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        points.sort()
        if (points[0][0] == points[1][0] and points[0][1] == points[1][1]) or (points[1][0] == points[2][0] and points[1][1] == points[2][1]):
            return False
        if points[0][0] == points[1][0]:
            return points[0][0] != points[2][0]
        if points[1][0] == points[2][0]:
            return points[0][0] != points[1][0]
        return (points[1][1] - points[0][1]) / (points[1][0] - points[0][0]) != (points[2][1] - points[1][1]) / (points[2][0] - points[1][0])