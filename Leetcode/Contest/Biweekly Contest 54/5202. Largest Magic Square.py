# https://leetcode.com/contest/biweekly-contest-54/problems/largest-magic-square/

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        result = 0
        for rowU in range(len(grid)):
            for colL in range(len(grid[0])):
                for size in range(result + 1, min(len(grid) - rowU, len(grid[0]) - colL) + 1):
                    isValid = True
                    magicSum = 0
                    for i in range(size):
                        magicSum += grid[rowU + i][colL + i]
                    temp = 0
                    for i in range(size):
                        temp += grid[rowU + size - 1 - i][colL + i]
                    if magicSum != temp:
                        continue
                    for row in range(rowU, rowU + size):
                        temp = sum(grid[row][colL:colL + size])
                        if magicSum != temp:
                            isValid = False
                            break
                    if not isValid:
                        continue
                    for col in range(colL, colL + size):
                        temp = 0
                        for row in range(rowU, rowU + size):
                            temp += grid[row][col]
                        if magicSum != temp:
                            isValid = False
                            break
                    if not isValid:
                        continue
                    result = size
        return result
