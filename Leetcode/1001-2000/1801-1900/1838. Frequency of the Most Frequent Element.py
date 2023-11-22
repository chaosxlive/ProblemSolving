# https://leetcode.com/problems/frequency-of-the-most-frequent-element/

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        resultFreq = 1
        left, right = 0, 0
        curUsed = 0
        while right < len(nums):
            if right == left:
                right += 1
                continue
            req = (nums[right] - nums[right - 1]) * (right - left)
            if curUsed + req <= k:
                curUsed += req
                resultFreq = max(resultFreq, right - left + 1)
                right += 1
            else:
                curUsed -= nums[right - 1] - nums[left]
                left += 1
        return resultFreq
