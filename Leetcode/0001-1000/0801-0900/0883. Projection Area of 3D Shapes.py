# https://leetcode.com/problems/projection-area-of-3d-shapes/

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        rows = [0] * len(grid)
        cols = [0] * len(grid[0])
        base = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                rows[row] = max(rows[row], grid[row][col])
                cols[col] = max(cols[col], grid[row][col])
                if grid[row][col]:
                    base += 1
        return sum(rows) + sum(cols) + base
