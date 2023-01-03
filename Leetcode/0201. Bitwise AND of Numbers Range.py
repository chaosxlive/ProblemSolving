# https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bit = 1 << 30
        result = 0
        while bit > 0 and (left & bit == right & bit):
            if left & bit > 0:
                result |= bit
            bit >>= 1
        return result
