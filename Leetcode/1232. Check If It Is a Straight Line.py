# https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[0][0] == coordinates[1][0]:
            for coordinate in coordinates[2:]:
                if coordinate[0] != coordinates[0][0]:
                    return False
        else:
            slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
            for coordinate in coordinates[2:]:
                if coordinate[0] == coordinates[0][0] or (coordinate[1] - coordinates[0][1]) / (coordinate[0] - coordinates[0][0]) != slope:
                    return False
        return True