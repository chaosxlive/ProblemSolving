# https://leetcode.com/problems/max-consecutive-ones/

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        i = 0
        while True:
            try:
                j = nums.index(0, i)
                result = max(result, j - i)
                i = j + 1
            except:
                result = max(result, len(nums) - i)
                break
        return result
