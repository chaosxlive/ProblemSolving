# https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            first = matrix[i][0]
            row, col = i, 0
            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != first:
                    return False
                row += 1
                col += 1
        for i in range(len(matrix[0])):
            first = matrix[0][i]
            row, col = 0, i
            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != first:
                    return False
                row += 1
                col += 1
        return True
