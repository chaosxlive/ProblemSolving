# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        isNeg = False
        if x < 0:
            isNeg = True
            x *= -1

        result = 0
        while x != 0:
            result = result * 10 + x % 10
            x //= 10

        if (not isNeg and result > 2147483647) or (isNeg and result > 2147483648):
            return 0

        return -1 * result if isNeg else result
