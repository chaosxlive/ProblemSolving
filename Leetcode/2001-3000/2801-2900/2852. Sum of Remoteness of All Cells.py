# https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

from typing import List
from collections import defaultdict


class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        uf = {}

        def find(x):
            if x not in uf:
                uf[x] = x
            elif uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                uf[rx] = ry

        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        total = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == -1:
                    continue
                curr = (row, col)
                total += grid[row][col]
                find(curr)
                for dr, dc in dirs:
                    if row + dr < 0 or \
                            row + dr >= len(grid) or \
                            col + dc < 0 or \
                            col + dc >= len(grid[0]) or \
                            grid[row + dr][col + dc] == -1:
                        continue
                    union(curr, (row + dr, col + dc))

        vs = defaultdict(int)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == -1:
                    continue
                vs[find((row, col))] += grid[row][col]

        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == -1:
                    continue
                result += total - vs[find((row, col))]
        return result
