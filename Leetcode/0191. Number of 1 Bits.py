# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        mask = 1
        for bit in range(32):
            if n & mask != 0:
                result += 1
            mask <<= 1
        return result
