# https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.result = 0
        self.grid = grid

        self.length = len(grid) * len(grid[0])
        startRow, StartCol = -1, -1
        hasStart = hasEnd = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == -1:
                    self.length -= 1
                    continue
                if grid[row][col] == 1:
                    startRow = row
                    StartCol = col
                    hasStart = True
                elif grid[row][col] == 2:
                    hasEnd = True
        if not hasStart or not hasEnd:
            return 0

        self.visit = [[False for col in range(len(grid[0]))] for row in range(len(grid))]

        self.dfs(startRow, StartCol, 1)

        return self.result

    def dfs(self, row, col, count):
        if self.visit[row][col] or self.grid[row][col] == -1:
            return
        if count == self.length and self.grid[row][col] == 2:
            self.result += 1
            return
        self.visit[row][col] = True

        if row > 0:
            self.dfs(row - 1, col, count + 1)
        if row < len(self.grid) - 1:
            self.dfs(row + 1, col, count + 1)
        if col > 0:
            self.dfs(row, col - 1, count + 1)
        if col < len(self.grid[0]) - 1:
            self.dfs(row, col + 1, count + 1)

        self.visit[row][col] = False