# https://leetcode.com/problems/making-a-large-island/

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        history = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        islandSize = {}

        def dfs(grid, history, islandSize, row, col, id):
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return
            if history[row][col] != 0 or grid[row][col] == 0:
                return

            history[row][col] = id
            islandSize[id] += 1
            for direction in directions:
                dfs(grid, history, islandSize, row + direction[0], col + direction[1], id)

        id = 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if history[row][col] == 0 and grid[row][col] == 1:
                    islandSize[id] = 0
                    dfs(grid, history, islandSize, row, col, id)
                    id += 1

        result = max(islandSize.values()) if len(islandSize) else 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if history[row][col] == 0:
                    temp = 0
                    seen = set()
                    for direction in directions:
                        if 0 <= row + direction[0] < len(history) and 0 <= col + direction[1] < len(history[0]):
                            if history[row + direction[0]][col + direction[1]] != 0 and history[row + direction[0]][col + direction[1]] not in seen:
                                temp += islandSize[history[row + direction[0]][col + direction[1]]]
                                seen.add(history[row + direction[0]][col + direction[1]])
                    result = max(result, temp + 1)
        return result
