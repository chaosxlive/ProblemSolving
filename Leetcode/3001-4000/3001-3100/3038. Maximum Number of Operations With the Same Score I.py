# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/

from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        result = 0
        for i in range(1, len(nums), 2):
            if nums[i] + nums[i - 1] == nums[0] + nums[1]:
                result += 1
            else:
                break
        return result
