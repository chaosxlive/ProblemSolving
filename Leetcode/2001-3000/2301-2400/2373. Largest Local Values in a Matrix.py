# https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        neighbors = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        result = []
        for row in range(1, len(grid) - 1):
            result.append([])
            for col in range(1, len(grid[0]) - 1):
                m = grid[row][col]
                for neighbor in neighbors:
                    m = max(m, grid[row + neighbor[0]][col + neighbor[1]])
                result[-1].append(m)
        return result
