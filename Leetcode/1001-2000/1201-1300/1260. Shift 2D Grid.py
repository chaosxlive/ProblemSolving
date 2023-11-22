# https://leetcode.com/problems/shift-2d-grid/

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        result = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        k %= len(grid) * len(grid[0])
        for index in range(len(grid) * len(grid[0])):
            sourceRow = (index // len(grid[0])) % len(grid)
            sourceCol = (index % len(grid[0])) % len(grid[0])
            targetRow = ((index + k) // len(grid[0])) % len(grid)
            targetCol = ((index + k) % len(grid[0])) % len(grid[0])
            result[targetRow][targetCol] = grid[sourceRow][sourceCol]
        return result
