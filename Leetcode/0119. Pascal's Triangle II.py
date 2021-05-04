# https://leetcode.com/problems/pascals-triangle-ii/

import math


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for k in range(rowIndex + 1):
            result.append(math.comb(rowIndex, k))
        return result