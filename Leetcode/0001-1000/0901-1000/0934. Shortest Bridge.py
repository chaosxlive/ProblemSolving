# https://leetcode.com/problems/shortest-bridge/

from typing import List
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        seen = set()
        q = deque()
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfsFindLand(row, col):
            for dr, dc in dirs:
                if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]) and grid[row + dr][col + dc] == 1 and (row + dr, col + dc) not in seen:
                    seen.add((row + dr, col + dc))
                    q.append((row + dr, col + dc, 0))
                    dfsFindLand(row + dr, col + dc)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    seen.add((row, col))
                    q.append((row, col, 0))
                    dfsFindLand(row, col)
                    break
            if len(q) > 0:
                break

        while len(q) > 0:
            row, col, step = q.popleft()
            for dr, dc in dirs:
                if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]):
                    if grid[row + dr][col + dc] == 0:
                        if (row + dr, col + dc) not in seen:
                            seen.add((row + dr, col + dc))
                            q.append((row + dr, col + dc, step + 1))
                    elif (row + dr, col + dc) not in seen:
                        return step
        return -1
