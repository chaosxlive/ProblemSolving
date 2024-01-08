# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        area = diag = 0
        for l, w in dimensions:
            d = (l ** 2 + w ** 2) ** 0.5
            if d == diag and l * w > area or d > diag:
                diag = d
                area = l * w
        return area
