# https://leetcode.com/problems/as-far-from-land-as-possible/

from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        hasLand = hasWater = False
        q = deque()
        seen = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    hasWater = True
                else:
                    hasLand = True
                    q.append((row, col, 0))
        if not hasLand or not hasWater:
            return -1
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        result = 0
        while len(q) > 0:
            row, col, step = q.popleft()
            for dr, dc in dirs:
                if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]) and grid[row + dr][col + dc] == 0 and (row + dr, col + dc) not in seen:
                    seen.add((row + dr, col + dc))
                    result = max(result, step + 1)
                    q.append((row + dr, col + dc, step + 1))
        return result
