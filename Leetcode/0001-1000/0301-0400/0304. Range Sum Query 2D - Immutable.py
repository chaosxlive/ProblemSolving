# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrixSum = [[0 for col in range(len(matrix[0]) + 1)] for row in range(len(matrix) + 1)]
        for rowIndex in range(1, len(matrix) + 1):
            rowSum = 0
            for colIndex in range(1, len(matrix[0]) + 1):
                rowSum += matrix[rowIndex - 1][colIndex - 1]
                self.matrixSum[rowIndex][colIndex] = rowSum + self.matrixSum[rowIndex - 1][colIndex]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrixSum[row2 + 1][col2 + 1] - self.matrixSum[row1][col2 + 1] - self.matrixSum[row2 + 1][col1] + self.matrixSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
