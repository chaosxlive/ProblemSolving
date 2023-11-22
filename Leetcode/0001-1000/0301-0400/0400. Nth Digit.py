# https://leetcode.com/problems/nth-digit/

class Solution:
    def findNthDigit(self, n: int) -> int:
        base = 1
        l = 1
        prev = 0
        while base * 9 * l < n:
            prev += base * 9 * l
            base *= 10
            l += 1
        rest = n - prev - 1
        q = rest // l
        m = rest % l
        return int(str(base + q)[m])
