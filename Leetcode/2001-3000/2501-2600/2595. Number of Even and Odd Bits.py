# https://leetcode.com/problems/number-of-even-and-odd-bits/

from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        result = [0, 0]
        bitCnt = 0
        while n > 0:
            result[bitCnt % 2] += n & 1
            n >>= 1
            bitCnt += 1
        return result
