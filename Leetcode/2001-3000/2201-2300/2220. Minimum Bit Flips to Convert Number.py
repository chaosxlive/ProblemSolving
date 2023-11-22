# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        cnt = 0
        bit = 1
        while start != goal:
            if (start & bit) ^ (goal & bit) > 0:
                cnt += 1
                start |= bit
                goal |= bit
            bit <<= 1
        return cnt