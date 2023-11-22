# https://leetcode.com/problems/semi-ordered-permutation/

from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        f = l = -1
        for i, n in enumerate(nums):
            if n == 1:
                f = i
            elif n == len(nums):
                l = i
        return f + len(nums) - l - 1 - (1 if f > l else 0)
