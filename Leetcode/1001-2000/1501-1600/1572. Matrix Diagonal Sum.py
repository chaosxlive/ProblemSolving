# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)
        result = 0
        for i in range(length):
            result += mat[i][i] + mat[i][length - i - 1]

        return result if length % 2 == 0 else result - mat[length // 2][length // 2]
