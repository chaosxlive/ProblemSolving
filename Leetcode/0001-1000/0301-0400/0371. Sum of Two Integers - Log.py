# https://leetcode.com/problems/sum-of-two-integers/

from math import log, exp


class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(log(exp(a) * exp(b)))
