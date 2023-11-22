# https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lower, upper = 0, 65536
        while True:
            center = (lower + upper) // 2
            if center * center == num:
                return True
            elif center * center > num:
                upper = center
            else:
                lower = center
            if lower + 1 == upper:
                return False
