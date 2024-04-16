# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

from typing import List


class Solution:

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        diffs = sorted(((num ^ k) - num for num in nums), reverse=True)
        s = sum(nums)
        for i in range(1, len(nums), 2):
            if diffs[i] + diffs[i - 1] > 0:
                s += diffs[i] + diffs[i - 1]
            else:
                break
        return s
