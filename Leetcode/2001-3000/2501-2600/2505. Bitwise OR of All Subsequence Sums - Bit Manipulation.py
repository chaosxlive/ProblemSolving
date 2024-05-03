# https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

from typing import List


class Solution:

    def subsequenceSumOr(self, nums: List[int]) -> int:
        bitCnt = [0] * 65
        res = 0
        for num in nums:
            for i in range(32):
                if num & (1 << i) > 0:
                    bitCnt[i] += 1
        for i in range(64):
            if bitCnt[i] > 0:
                res |= 1 << i
            bitCnt[i + 1] += bitCnt[i] // 2
        return res
