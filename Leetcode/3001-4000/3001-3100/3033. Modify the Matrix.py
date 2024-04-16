# https://leetcode.com/problems/modify-the-matrix/

from typing import List


class Solution:

    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        ret = [[C for C in R] for R in matrix]
        M = [max(matrix[i][c] for i in range(len(matrix))) for c in range(len(matrix[0]))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if ret[r][c] == -1:
                    ret[r][c] = M[c]
        return ret
