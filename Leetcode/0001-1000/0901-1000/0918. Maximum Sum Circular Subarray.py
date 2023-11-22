# https://leetcode.com/problems/maximum-sum-circular-subarray/

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Case 1:
        #   It doesn't contain circular part.
        # Case 2:
        #   It contains circular part, so we find the reverse of minimum of non-circular subarray.
        generalMin = generalMax = nums[0]
        currentMin = currentMax = total = 0
        for num in nums:
            currentMax = max(currentMax + num, num)
            generalMax = max(generalMax, currentMax)
            currentMin = min(currentMin + num, num)
            generalMin = min(generalMin, currentMin)
            total += num
        return max(total - generalMin, generalMax) if generalMax > 0 else generalMax
