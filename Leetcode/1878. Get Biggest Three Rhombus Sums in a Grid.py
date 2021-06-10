# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        countRow, countCol = len(grid), len(grid[0])
        sumRT = [[0 for col in range(countCol + 2)] for row in range(countRow + 2)]
        sumLT = [[0 for col in range(countCol + 2)] for row in range(countRow + 2)]
        max1 = max2 = max3 = 0
        for row in range(countRow):
            for col in range(countCol):
                if grid[row][col] not in [max1, max2, max3]:
                    if grid[row][col] > max1:
                        max1, max2, max3 = grid[row][col], max1, max2
                    elif grid[row][col] > max2:
                        max2, max3 = grid[row][col], max2
                    elif grid[row][col] > max3:
                        max3 = grid[row][col]
                sumRT[row + 1][col + 1] = grid[row][col] + sumRT[row][col]
                sumLT[row + 1][col + 1] = grid[row][col] + sumLT[row][col + 2]
        for size in range(1, (min(countRow, countCol) + 1) // 2):
            for row in range(size + 1, countRow - size + 1):
                for col in range(size + 1, countCol - size + 1):
                    curSum = 0
                    curSum += sumRT[row][col + size] - sumRT[row - size - 1][col - 1]
                    curSum += sumRT[row + size][col] - sumRT[row - 1][col - size - 1]
                    curSum += sumLT[row][col - size] - sumLT[row - size - 1][col + 1]
                    curSum += sumLT[row + size][col] - sumLT[row - 1][col + size + 1]
                    curSum -= grid[row - size - 1][col - 1] + grid[row + size - 1][col - 1] + grid[row - 1][col - size - 1] + grid[row - 1][col + size - 1]
                    if curSum not in [max1, max2, max3]:
                        if curSum > max1:
                            max1, max2, max3 = curSum, max1, max2
                        elif curSum > max2:
                            max2, max3 = curSum, max2
                        elif curSum > max3:
                            max3 = curSum
        if max2 == 0:
            return [max1]
        if max3 == 0:
            return [max1, max2]
        return [max1, max2, max3]
