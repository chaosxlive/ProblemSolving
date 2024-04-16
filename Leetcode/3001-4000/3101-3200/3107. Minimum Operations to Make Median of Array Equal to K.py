# https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

from typing import List


class Solution:

    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        L = len(nums)
        res = 0
        if L % 2 == 0:
            for i in range(L // 2 - 1):
                if nums[i] > k:
                    res += nums[i] - k
                if nums[-i - 1] < k:
                    res += k - nums[-i - 1]
            if nums[L // 2 - 1] > k:
                res += nums[L // 2 - 1] - k
            res += abs(nums[L // 2] - k)
        else:
            for i in range(L // 2):
                if nums[i] > k:
                    res += nums[i] - k
                if nums[-i - 1] < k:
                    res += k - nums[-i - 1]
            res += abs(nums[L // 2] - k)
        return res
