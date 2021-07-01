# https://leetcode.com/contest/weekly-contest-246/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = [[False for col in range(len(grid1[0]))] for row in range(len(grid1))]

        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                if grid2[row][col] == 1:
                    grid2[row][col] += grid1[row][col]
                elif grid2[row][col] == 0:
                    visited[row][col] = True

        def dfs(visited, row, col):
            visited[row][col] = True
            result = grid2[row][col] != 1
            if row - 1 >= 0 and not visited[row - 1][col]:
                if not dfs(visited, row - 1, col):
                    result = False
            if row + 1 < len(grid1) and not visited[row + 1][col]:
                if not dfs(visited, row + 1, col):
                    result = False
            if col - 1 >= 0 and not visited[row][col - 1]:
                if not dfs(visited, row, col - 1):
                    result = False
            if col + 1 < len(grid1[0]) and not visited[row][col + 1]:
                if not dfs(visited, row, col + 1):
                    result = False
            return result

        result = 0
        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                if not visited[row][col] and dfs(visited, row, col):
                    result += 1
        return result
