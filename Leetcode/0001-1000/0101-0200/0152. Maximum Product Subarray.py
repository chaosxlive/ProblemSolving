# https://leetcode.com/problems/maximum-product-subarray/

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMax = currentMin = generalMax = nums[0]
        hasZero = nums[0] == 0
        for idx, num in enumerate(nums):
            if idx == 0:
                continue
            if num == 0:
                hasZero = True
                currentMax = currentMin = 1
                generalMax = max(0, generalMax)
            else:
                currentMin, currentMax = min(currentMax * num, currentMin * num, num), max(currentMax * num, currentMin * num, num)
                generalMax = max(currentMax, currentMin, generalMax)
        return max(generalMax, 0) if hasZero else generalMax
