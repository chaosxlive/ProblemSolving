# https://leetcode.com/problems/mirror-reflection/

import math


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcm = (p * q) // math.gcd(p, q)
        a = lcm // p
        b = lcm // q
        if (a + b) % 2 == 0:
            return 1
        if a % 2 == 0:
            return 0
        return 2
