# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

from typing import List


class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(1 for n in nums if n < k)
