# https://leetcode.com/problems/row-with-maximum-ones/

from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        result = [-1, -1]
        for i, row in enumerate(mat):
            cnt = sum(row)
            if cnt > result[1]:
                result = [i, cnt]
        return result
