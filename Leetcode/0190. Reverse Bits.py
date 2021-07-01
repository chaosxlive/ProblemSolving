# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        mask, ptr = 1, 1 << 31
        result = 0
        for bit in range(32):
            if n & mask != 0:
                result |= ptr
            mask <<= 1
            ptr >>= 1
        return result
