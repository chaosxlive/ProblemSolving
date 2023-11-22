# https://leetcode.com/problems/armstrong-number/

import math


class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = math.floor(math.log10(n)) + 1
        temp = n
        s = 0
        while temp > 0:
            s += (temp % 10) ** k
            temp //= 10
        return s == n
