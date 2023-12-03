# https://leetcode.com/problems/largest-submatrix-with-rearrangements/

from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ones = [[0] * len(matrix) for _ in matrix[0]]
        for c in range(len(matrix[0])):
            if matrix[len(matrix) - 1][c] == 1:
                ones[c][len(matrix) - 1] = 1
            for r in reversed(range(len(matrix) - 1)):
                if matrix[r][c] == 1:
                    ones[c][r] = 1 + ones[c][r + 1]
        result = 0
        for j in range(len(ones[0])):
            ones.sort(key=lambda x: x[j], reverse=True)
            for i in range(len(ones)):
                result = max(result, ones[i][j] * (i + 1))
        return result
