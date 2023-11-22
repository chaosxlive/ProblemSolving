# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List
from bisect import bisect_left


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            idx = bisect_left(row, target)
            if idx < len(row) and row[idx] == target:
                return True
        return False
