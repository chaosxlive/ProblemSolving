# https://leetcode.com/problems/max-area-of-island/

import queue


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        result = 0
        bfs = queue.SimpleQueue()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and visited[row][col] == 0:
                    bfs.put([row, col])
                    visited[row][col] = 1
                    count = 1
                    while not bfs.empty():
                        current = bfs.get()
                        if current[0] > 0 and grid[current[0] - 1][current[1]] == 1 and visited[current[0] - 1][current[1]] == 0:
                            bfs.put([current[0] - 1, current[1]])
                            visited[current[0] - 1][current[1]] = 1
                            count += 1
                        if current[0] < len(grid) - 1 and grid[current[0] + 1][current[1]] == 1 and visited[current[0] + 1][current[1]] == 0:
                            bfs.put([current[0] + 1, current[1]])
                            visited[current[0] + 1][current[1]] = 1
                            count += 1
                        if current[1] > 0 and grid[current[0]][current[1] - 1] == 1 and visited[current[0]][current[1] - 1] == 0:
                            bfs.put([current[0], current[1] - 1])
                            visited[current[0]][current[1] - 1] = 1
                            count += 1
                        if current[1] < len(grid[0]) - 1 and grid[current[0]][current[1] + 1] == 1 and visited[current[0]][current[1] + 1] == 0:
                            bfs.put([current[0], current[1] + 1])
                            visited[current[0]][current[1] + 1] = 1
                            count += 1
                    result = max(result, count)
        return result
