# https://leetcode.com/problems/max-consecutive-ones-ii/

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        iZero = 0
        try:
            iZero = nums.index(0)
        except:
            pass
        if iZero == len(nums):
            return len(nums)
        nums.append(0)
        prev1s = iZero
        result = prev1s
        i = iZero + 1
        while i < len(nums):
            if nums[i] == 0:
                result = max(result, prev1s + i - iZero)
                prev1s = i - iZero - 1
                iZero = i
            i += 1
        return result
