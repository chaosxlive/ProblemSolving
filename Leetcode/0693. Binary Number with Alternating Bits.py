# https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        isOdd = (n % 4 == 1)
        while n > 0:
            if isOdd and n % 4 != 1:
                return False
            if not isOdd and n % 4 != 2:
                return False
            n >>= 2
        return True
