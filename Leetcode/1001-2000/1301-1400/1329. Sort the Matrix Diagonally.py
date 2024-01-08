# https://leetcode.com/problems/sort-the-matrix-diagonally/

from collections import defaultdict
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        n = defaultdict(int)
        for r, R in enumerate(mat):
            for c, C in enumerate(R):
                d[r - c].append(C)
        for l in d.values():
            l.sort()
        for r, R in enumerate(mat):
            for c, C in enumerate(R):
                mat[r][c] = d[r - c][n[r - c]]
                n[r - c] += 1
        return mat
