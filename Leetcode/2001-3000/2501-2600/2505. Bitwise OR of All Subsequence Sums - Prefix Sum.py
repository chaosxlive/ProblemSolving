# https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

from typing import List


class Solution:

    def subsequenceSumOr(self, nums: List[int]) -> int:
        res = 0
        s = 0
        for num in nums:
            s += num
            res |= num | s
        return res
