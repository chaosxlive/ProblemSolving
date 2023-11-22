# https://leetcode.com/problems/find-the-k-or-of-an-array/

from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        bitCnts = [0] * 32
        for num in nums:
            for b in range(0, 31):
                if num & (1 << b) > 0:
                    bitCnts[b] += 1
        result = 0
        for b in range(0, 31):
            if bitCnts[b] >= k:
                result += 1 << b
        return result
