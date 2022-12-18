# https://leetcode.com/problems/subarray-product-less-than-k/

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right = -1, 0
        multiplied = 1
        result = 0
        while right < len(nums):
            if multiplied * nums[right] < k:
                multiplied *= nums[right]
                right += 1
            elif left + 1 < right:
                result += right - left - 1
                left += 1
                multiplied //= nums[left]
            else:
                left += 1
                right += 1
        rest = len(nums) - left - 1
        result += (1 + rest) * rest // 2
        return result
