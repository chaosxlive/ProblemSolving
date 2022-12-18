# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = -1, 0
        total = 0
        result = 100001
        while right < len(nums):
            total += nums[right]
            if total >= target:
                while total - nums[left + 1] >= target:
                    left += 1
                    total -= nums[left]
                result = min(result, right - left)
            right += 1
        return 0 if result == 100001 else result
