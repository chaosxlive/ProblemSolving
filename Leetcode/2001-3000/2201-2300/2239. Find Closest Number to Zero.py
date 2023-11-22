# https://leetcode.com/problems/find-closest-number-to-zero/

from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        resultIdx = 0
        for i in range(1, len(nums)):
            if abs(nums[i]) < abs(nums[resultIdx]):
                resultIdx = i
            elif abs(nums[i]) == abs(nums[resultIdx]) and nums[i] > nums[resultIdx]:
                resultIdx = i
        return nums[resultIdx]
