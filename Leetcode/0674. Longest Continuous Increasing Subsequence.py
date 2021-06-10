# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 1
        current = 1
        for index in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                current += 1
            else:
                result = max(current, result)
                current = 1
        return max(current, result)