# https://leetcode.com/problems/number-of-islands/

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        seen = set()
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(row, col):
            seen.add((row, col))
            for dr, dc in dirs:
                if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]) and grid[row + dr][col + dc] == '1' and (row + dr, col + dc) not in seen:
                    dfs(row + dr, col + dc)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    if (row, col) not in seen:
                        result += 1
                    dfs(row, col)
        return result
