# https://leetcode.com/problems/surface-area-of-3d-shapes/

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        result = len(grid) * len(grid[0]) * 2
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    result -= 2

                result += grid[row][col] * 4

                if row > 0:
                    result -= min(grid[row][col], grid[row - 1][col])
                if row < len(grid) - 1:
                    result -= min(grid[row][col], grid[row + 1][col])
                if col > 0:
                    result -= min(grid[row][col], grid[row][col - 1])
                if col < len(grid[0]) - 1:
                    result -= min(grid[row][col], grid[row][col + 1])
        return result
