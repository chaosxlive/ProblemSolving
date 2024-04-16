from math import ceil, inf
from typing import Optional, List


class Solution:

    def minOperations(self, k: int) -> int:
        res = inf
        i = 0
        while i < k:
            ops = i
            n = 1 + ops

            if n >= k:
                res = min(res, ops)
            else:
                res = min(res, ops + ceil(k / n) - 1)
            i += 1
        return res
