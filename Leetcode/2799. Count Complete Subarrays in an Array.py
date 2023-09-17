# https://leetcode.com/problems/count-complete-subarrays-in-an-array/

from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        result = 0
        totalDistinct = len(set(nums))
        for start in range(len(nums)):
            distinct = set()
            for i in range(start, len(nums)):
                if nums[i] not in distinct:
                    distinct.add(nums[i])
                if len(distinct) == totalDistinct:
                    result += 1
        return result
