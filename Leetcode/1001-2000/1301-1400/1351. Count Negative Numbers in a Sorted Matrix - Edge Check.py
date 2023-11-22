# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        ptrRow = 0
        ptrCol = len(grid[0]) - 1

        while ptrCol >= 0 and ptrRow < len(grid):
            if grid[ptrRow][ptrCol] >= 0:
                ptrRow += 1
            else:
                result += len(grid) - ptrRow
                ptrCol -= 1
        
        return result
