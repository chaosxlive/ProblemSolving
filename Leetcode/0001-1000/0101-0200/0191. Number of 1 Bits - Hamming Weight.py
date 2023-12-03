# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        m1 = 0x55555555
        m2 = 0x33333333
        m4 = 0x0f0f0f0f
        m8 = 0x00ff00ff
        m16 = 0x0000ffff
        n = (n & m1) + ((n >> 1) & m1)
        n = (n & m2) + ((n >> 2) & m2)
        n = (n & m4) + ((n >> 4) & m4)
        n = (n & m8) + ((n >> 8) & m8)
        n = (n & m16) + ((n >> 16) & m16)
        return n
