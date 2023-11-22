# https://leetcode.com/problems/count-servers-that-communicate/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = [0] * len(grid)
        cols = [0] * len(grid[0])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    rows[row] += 1
                    cols[col] += 1

        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if rows[row] > 1 or cols[col] > 1:
                        result += 1
        return result

