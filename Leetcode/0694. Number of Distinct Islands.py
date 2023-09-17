# https://leetcode.com/problems/number-of-distinct-islands/

from typing import List
import json


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        seen = set()
        dirs = (
            (lambda x: x + 1, 0, 1),
            (lambda x: x - 1, 0, -1),
            (lambda x: x + len(grid[0]) + 1, 1, 0),
            (lambda x: x - len(grid[0]) - 1, -1, 0)
        )

        def dfs(r, c, shape, id):
            seen.add((r, c))
            shape.add(id)
            for (f, dr, dc) in dirs:
                if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]) and grid[r + dr][c + dc] == 1:
                    if (r + dr, c + dc) not in seen:
                        dfs(r + dr, c + dc, shape, f(id))
            if id == 0:
                islands.add(json.dumps(list(shape)))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in seen:
                    dfs(r, c, set(), 0)

        return len(islands)
