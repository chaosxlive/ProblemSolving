# https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/

from typing import List


class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        n = min(nums)
        return 0 if n == 100 else 1 if ((n // 10) + n) % 2 == 0 else 0
