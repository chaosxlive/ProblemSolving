# https://leetcode.com/problems/longest-increasing-subsequence/

import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        potential = []
        bestIndex = [0] * len(nums)
        result = 0
        for i in range(len(nums)):
            index = bisect.bisect_left(potential, nums[i])
            if index >= len(potential):
                potential.append(nums[i])
            else:
                potential[index] = nums[i]
            bestIndex[i] = index
            result = max(result, bestIndex[i])
        return result + 1
