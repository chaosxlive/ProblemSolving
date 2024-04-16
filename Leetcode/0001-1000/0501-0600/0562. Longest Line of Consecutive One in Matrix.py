# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

from typing import List


class Solution:

    def longestLine(self, mat: List[List[int]]) -> int:
        LR = len(mat)
        LC = len(mat[0])
        result = 0
        rs = [0] * LR
        cs = [0] * LC
        diags = [0] * (LR + LC - 1)
        antidiags = [0] * (LR + LC - 1)
        bias = LR - 1
        for r, R in enumerate(mat):
            for c, C in enumerate(R):
                if C == 1:
                    rs[r] += 1
                    cs[c] += 1
                    diags[c - r + bias] += 1
                    antidiags[r + c] += 1
                else:
                    result = max(result, rs[r], cs[c], diags[c - r + bias], antidiags[r + c])
                    rs[r] = 0
                    cs[c] = 0
                    diags[c - r + bias] = 0
                    antidiags[r + c] = 0
        return max(result, max(rs), max(cs), max(diags), max(antidiags))
