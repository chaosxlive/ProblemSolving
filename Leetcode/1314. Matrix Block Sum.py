# https://leetcode.com/problems/matrix-block-sum/

from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefixSum = [[0] * (len(mat[0]) + 1) for i in range(len(mat) + 1)]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                prefixSum[row + 1][col + 1] = prefixSum[row + 1][col] + prefixSum[row][col + 1] - prefixSum[row][col] + mat[row][col]
        result = [[0] * len(mat[0]) for i in range(len(mat))]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                rowTop, rowBottom = max(0, row - k), min(len(mat) - 1, row + k)
                colLeft, colRight = max(0, col - k), min(len(mat[0]) - 1, col + k)
                result[row][col] = prefixSum[rowBottom + 1][colRight + 1] - prefixSum[rowTop][colRight + 1] - prefixSum[rowBottom + 1][colLeft] + prefixSum[rowTop][colLeft]
        return result
