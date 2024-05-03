# https://leetcode.com/problems/island-perimeter/

from collections import deque
from typing import List


class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = col = 0
        while grid[row][col] == 0:
            col += 1
            if col == len(grid[0]):
                col = 0
                row += 1

        visited = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        result = 0
        dq = deque([[row, col]])
        visited[row][col] = 1
        while dq:
            r, c = dq.popleft()
            if r == 0 or (grid[r - 1][c]) == 0:
                result += 1
            elif visited[r - 1][c] == 0:
                dq.append([r - 1, c])
                visited[r - 1][c] = 1
            if r == len(grid) - 1 or (grid[r + 1][c]) == 0:
                result += 1
            elif visited[r + 1][c] == 0:
                dq.append([r + 1, c])
                visited[r + 1][c] = 1
            if c == 0 or (grid[r][c - 1]) == 0:
                result += 1
            elif visited[r][c - 1] == 0:
                dq.append([r, c - 1])
                visited[r][c - 1] = 1
            if c == len(grid[0]) - 1 or (grid[r][c + 1]) == 0:
                result += 1
            elif visited[r][c + 1] == 0:
                dq.append([r, c + 1])
                visited[r][c + 1] = 1
        return result
