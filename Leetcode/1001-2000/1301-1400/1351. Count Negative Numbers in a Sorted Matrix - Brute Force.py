# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        for row in grid:
            for col in row:
                if col < 0:
                    result += 1
        
        return result