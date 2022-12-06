# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        idx = 0
        while idx < len(nums) and nums[idx] < 0 and k > 0:
            nums[idx] *= -1
            k -= 1
            idx += 1
        if k % 2 == 1:
            nums.sort()
            nums[0] *= -1
        return sum(nums)
