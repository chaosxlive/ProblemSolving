# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
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
