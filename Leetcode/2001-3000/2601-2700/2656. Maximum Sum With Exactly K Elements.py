# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        n = max(nums)
        return (n + (n + k - 1)) * k // 2
