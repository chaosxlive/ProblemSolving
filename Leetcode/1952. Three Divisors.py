# https://leetcode.com/problems/three-divisors/

from math import isqrt


class Solution:
    def isThree(self, n: int) -> bool:
        t = isqrt(n)

        if t == 1:
            return False
        if t == 2:
            return True
        if t % 2 == 0:
            return False

        for i in range(3, isqrt(t) + 1, 2):
            if t % i == 0:
                return False

        return t**2 == n
