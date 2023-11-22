# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        result = False
        mask = 1
        for bit in range(32):
            if n & mask != 0:
                if result:
                    return False
                result = True
            mask <<= 1
        return result