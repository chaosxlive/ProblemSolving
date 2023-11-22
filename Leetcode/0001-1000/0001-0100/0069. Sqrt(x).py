# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        lower, upper = 0, 65536
        while True:
            center = (lower + upper) // 2
            if center * center == x:
                return center
            elif center * center > x:
                upper = center
            else:
                lower = center
            if lower + 1 == upper:
                return lower
        