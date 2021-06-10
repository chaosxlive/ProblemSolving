# https://leetcode.com/contest/weekly-contest-244/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        def rotate(matrix):
            length = len(matrix)
            half = length // 2
            for row in range(half):
                for col in range(half):
                    matrix[row][col], matrix[col][length - 1 - row], matrix[length - 1 - row][length - 1 - col], matrix[length - 1 - col][row] = \
                        matrix[length - 1 - col][row], matrix[row][col], matrix[col][length - 1 - row], matrix[length - 1 - row][length - 1 - col]

            if length % 2 == 1:
                for i in range(half):
                    matrix[half][i], matrix[i][half], matrix[half][length - 1 - i], matrix[length - 1 - i][half] = \
                        matrix[length - 1 - i][half], matrix[half][i], matrix[i][half], matrix[half][length - 1 - i]
        
        def check(matrix, target):
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    if matrix[row][col] != target[row][col]:
                        return False
            return True
        
        for i in range(4):
            rotate(mat)
            if check(mat, target):
                return True
        return False