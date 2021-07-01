# https://leetcode.com/contest/weekly-contest-247/problems/cyclically-rotating-a-grid/

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        layers = []
        for l in range(min(len(grid) // 2, len(grid[0]) // 2)):
            layers.append([])
            for row in range(l, len(grid) - l):
                layers[l].append(grid[row][l])
            for col in range(l + 1, len(grid[0]) - l - 1):
                layers[l].append(grid[-1 - l][col])
            for row in range(len(grid) - l - 1, l - 1, -1):
                layers[l].append(grid[row][-l - 1])
            for col in range(len(grid[0]) - l - 2, l, -1):
                layers[l].append(grid[l][col])
        result = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        for l in range(min(len(grid) // 2, len(grid[0]) // 2)):
            ptr = -k
            for row in range(l, len(grid) - l):
                result[row][l] = layers[l][ptr % len(layers[l])]
                ptr += 1
            for col in range(l + 1, len(grid[0]) - l - 1):
                result[-1 - l][col] = layers[l][ptr % len(layers[l])]
                ptr += 1
            for row in range(len(grid) - l - 1, l - 1, -1):
                result[row][-l - 1] = layers[l][ptr % len(layers[l])]
                ptr += 1
            for col in range(len(grid[0]) - l - 2, l, -1):
                result[l][col] = layers[l][ptr % len(layers[l])]
                ptr += 1
        return result
