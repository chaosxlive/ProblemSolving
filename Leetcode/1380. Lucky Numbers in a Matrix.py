# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_matrix = [[False for col in range(len(matrix[0]))] for row in range(len(matrix))]

        for row_index in range(len(matrix)):
            curMin = 1000001
            minIndex = -1
            for col_index in range(len(matrix[0])):
                if matrix[row_index][col_index] < curMin:
                    curMin = matrix[row_index][col_index]
                    minIndex = col_index
            min_matrix[row_index][minIndex] = True
            
        result = []

        for col_index in range(len(matrix[0])):
            curMax = 0
            maxIndex = -1
            for row_index in range(len(matrix)):
                if matrix[row_index][col_index] > curMax:
                    curMax = matrix[row_index][col_index]
                    maxIndex = row_index
            if min_matrix[maxIndex][col_index]:
                result.append(matrix[maxIndex][col_index])
        return result
