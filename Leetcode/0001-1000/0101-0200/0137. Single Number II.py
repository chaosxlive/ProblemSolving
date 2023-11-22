# https://leetcode.com/problems/single-number-ii/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0] * 32
        minusCnt = 0
        for num in nums:
            i = 0
            if num < 0:
                minusCnt += 1
                num *= -1
            while num > 0:
                if num & 1 > 0:
                    bits[i] += 1
                i += 1
                num >>= 1

        return int(''.join(reversed(['1' if bit % 3 > 0 else '0' for bit in bits])), 2) * (-1 if minusCnt % 3 > 0 else 1)
