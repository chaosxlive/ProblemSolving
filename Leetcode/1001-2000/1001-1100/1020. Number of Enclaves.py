# https://leetcode.com/problems/number-of-enclaves/

from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        seen = set()
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(row, col):
            seen.add((row, col))
            result = 1
            for dr, dc in dirs:
                if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]):
                    if grid[row + dr][col + dc] == 1 and (row + dr, col + dc) not in seen:
                        if result == -1:
                            dfs(row + dr, col + dc)
                        else:
                            res = dfs(row + dr, col + dc)
                            if res == -1:
                                result = -1
                            else:
                                result += res
                else:
                    result = -1
            return result

        result = 0
        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in seen:
                    res = dfs(row, col)
                    if res != -1:
                        result += res
        return result
