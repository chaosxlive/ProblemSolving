# https://leetcode.com/problems/3sum-smaller/

from typing import List


class Solution:

    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        def twoSumSmaller(left, right, t):
            res = 0
            while left < right:
                if nums[left] + nums[right] >= t:
                    right -= 1
                else:
                    res += right - left
                    left += 1
            return res

        nums.sort()
        result = 0
        for i in range(len(nums) - 2):
            result += twoSumSmaller(i + 1, len(nums) - 1, target - nums[i])
        return result
