# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/

from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        L = len(nums)
        frontIdx = 0
        while frontIdx + 1 < L and nums[frontIdx] < nums[frontIdx + 1]:
            frontIdx += 1

        if frontIdx == L - 1:
            return (1 + L) * L // 2

        backIdx = L - 1
        while backIdx >= 0 and nums[backIdx - 1] < nums[backIdx]:
            backIdx -= 1

        left = 0
        right = backIdx
        result = L - right + 1
        while left <= frontIdx and right < len(nums):
            if nums[right] <= nums[left]:
                right += 1
                if right == len(nums):
                    result += frontIdx - left + 1
            else:
                result += L - right + 1
                left += 1

        return result
