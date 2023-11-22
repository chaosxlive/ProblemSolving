# https://leetcode.com/problems/counting-bits/

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        top = 1
        bias = 1
        for i in range(1, n + 1):
            result[i] = result[i - bias] + 1
            if i == top:
                top = 2 * top + 1
                bias *= 2
        return result
