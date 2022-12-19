# https://leetcode.com/problems/shortest-path-in-binary-matrix/

from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1]:
            return -1
        if len(grid) == 1 and len(grid[0]) == 1:
            return 1
        q = deque()
        seen = set()
        q.append((0, 0, 1))
        dirs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        while len(q) > 0:
            row, col, step = q.popleft()
            for dr, dc in dirs:
                if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]) and grid[row + dr][col + dc] == 0 and (row + dr, col + dc) not in seen:
                    if (row + dr, col + dc) == (len(grid) - 1, len(grid[0]) - 1):
                        return step + 1
                    seen.add((row + dr, col + dc))
                    q.append((row + dr, col + dc, step + 1))
        return -1
