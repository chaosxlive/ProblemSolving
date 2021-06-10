# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRows = zeroCols = False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                zeroRows = True
                break
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                zeroCols = True
                break
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = matrix[row][0] = 0
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        if zeroRows:
            for row in range(len(matrix)):
                matrix[row][0] = 0
        if zeroCols:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
