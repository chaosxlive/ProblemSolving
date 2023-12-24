# https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        minIdx = maxIdx = 0
        for i in range(indexDifference, len(nums)):
            if nums[i - indexDifference] <= nums[minIdx]:
                minIdx = i - indexDifference
            if nums[i - indexDifference] >= nums[maxIdx]:
                maxIdx = i - indexDifference
            if abs(nums[i] - nums[maxIdx]) >= valueDifference:
                return [i, maxIdx]
            if abs(nums[i] - nums[minIdx]) >= valueDifference:
                return [i, minIdx]
        return [-1, -1]
