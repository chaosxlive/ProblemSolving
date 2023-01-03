# https://leetcode.com/problems/integer-break/

from math import pow


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        q = n // 3
        m = n % 3
        if m == 0:
            return int(pow(3, q))
        elif m == 1:
            return int(pow(3, q - 1) * 4)
        return int(pow(3, q) * 2)
