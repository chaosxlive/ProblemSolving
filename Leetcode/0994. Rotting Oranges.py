# https://leetcode.com/problems/rotting-oranges/

from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.append((row, col, 0))
        result = 0
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while q:
            row, col, step = q.popleft()
            result = max(result, step)
            for dr, dc in dirs:
                if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]) and grid[row + dr][col + dc] == 1:
                    grid[row + dr][col + dc] = 2
                    q.append((row + dr, col + dc, step + 1))
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
        return result
