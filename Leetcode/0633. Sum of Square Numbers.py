# https://leetcode.com/problems/sum-of-square-numbers/

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(math.floor(math.sqrt(c)) + 1):
            rest = c - i * i
            if math.floor(math.sqrt(rest)) ** 2 == rest:
                return True
        return False
