# https://leetcode.com/problems/island-perimeter/

import queue


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
        bfs = queue.SimpleQueue()
        bfs.put([row, col])
        visited[row][col] = 1
        while not bfs.empty():
            current = bfs.get()
            if current[0] == 0 or (grid[current[0] - 1][current[1]]) == 0:
                result += 1
            elif visited[current[0] - 1][current[1]] == 0:
                bfs.put([current[0] - 1, current[1]])
                visited[current[0] - 1][current[1]] = 1
            if current[0] == len(grid) - 1 or (grid[current[0] + 1][current[1]]) == 0:
                result += 1
            elif visited[current[0] + 1][current[1]] == 0:
                bfs.put([current[0] + 1, current[1]])
                visited[current[0] + 1][current[1]] = 1
            if current[1] == 0 or (grid[current[0]][current[1] - 1]) == 0:
                result += 1
            elif visited[current[0]][current[1] - 1] == 0:
                bfs.put([current[0], current[1] - 1])
                visited[current[0]][current[1] - 1] = 1
            if current[1] == len(grid[0]) - 1 or (grid[current[0]][current[1] + 1]) == 0:
                result += 1
            elif visited[current[0]][current[1] + 1] == 0:
                bfs.put([current[0], current[1] + 1])
                visited[current[0]][current[1] + 1] = 1
        return result
