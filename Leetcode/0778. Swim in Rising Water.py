# https://leetcode.com/problems/swim-in-rising-water/

import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = [[False for col in range(len(grid[0]))] for row in range(len(grid))]
        time = 0
        next = [(grid[0][0], 0, 0)]
        visited[0][0] = True

        def dfs(grid, visited, next, row, col):
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return True

            if row + 1 < len(grid) and not visited[row + 1][col]:
                visited[row + 1][col] = True
                if grid[row + 1][col] > time:
                    heapq.heappush(next, (grid[row + 1][col], row + 1, col))
                elif dfs(grid, visited, next, row + 1, col):
                    return True
            if row - 1 >= 0 and not visited[row - 1][col]:
                visited[row - 1][col] = True
                if grid[row - 1][col] > time:
                    heapq.heappush(next, (grid[row - 1][col], row - 1, col))
                elif dfs(grid, visited, next, row - 1, col):
                    return True
            if col + 1 < len(grid[0]) and not visited[row][col + 1]:
                visited[row][col + 1] = True
                if grid[row][col + 1] > time:
                    heapq.heappush(next, (grid[row][col + 1], row, col + 1))
                elif dfs(grid, visited, next, row, col + 1):
                    return True
            if col - 1 >= 0 and not visited[row][col - 1]:
                visited[row][col - 1] = True
                if grid[row][col - 1] > time:
                    heapq.heappush(next, (grid[row][col - 1], row, col - 1))
                elif dfs(grid, visited, next, row, col - 1):
                    return True
            return False

        while len(next) != 0:
            nextTime = heapq.heappop(next)
            time = nextTime[0]
            if nextTime[1] == len(grid) - 1 and nextTime[2] == len(grid[0]) - 1:
                return time
            if dfs(grid, visited, next, nextTime[1], nextTime[2]):
                return time
