# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rr = [0] * len(mat)
        rc = [0] * len(mat[0])
        for rowIdx in range(len(mat)):
            for colIdx in range(len(mat[0])):
                if mat[rowIdx][colIdx] == 1:
                    rr[rowIdx] += 1
                    rc[colIdx] += 1
        result = 0
        for rowIdx in range(len(mat)):
            for colIdx in range(len(mat[0])):
                if mat[rowIdx][colIdx] == 1 and rr[rowIdx] == 1 and rc[colIdx] == 1:
                    result += 1
        return result
