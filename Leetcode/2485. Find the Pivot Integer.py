# https://leetcode.com/problems/find-the-pivot-integer/

import math


class Solution:
    def pivotInteger(self, n: int) -> int:
        s2 = (n * n + n) // 2
        s = math.isqrt(s2)
        return s if s * s == s2 else -1
