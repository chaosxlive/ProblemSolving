# https://leetcode.com/problems/sum-of-squares-of-special-elements/

from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(v*v for i, v in enumerate(nums) if len(nums) % (i + 1) == 0)
