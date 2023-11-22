# https://leetcode.com/problems/number-of-closed-islands/

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(row, col):
            seen.add((row, col))
            isSurrounded = True
            for dr, dc in dirs:
                if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]):
                    if grid[row + dr][col + dc] == 0 and (row + dr, col + dc) not in seen:
                        isSurrounded = dfs(row + dr, col + dc) and isSurrounded
                else:
                    isSurrounded = False
            return isSurrounded

        result = 0
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0]) - 1):
                if grid[row][col] == 0 and (row, col) not in seen and dfs(row, col):
                    result += 1
        return result
