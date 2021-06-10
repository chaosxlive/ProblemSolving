# https://leetcode.com/contest/biweekly-contest-53/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums) // 2):
            result = max(result, nums[i] + nums[-i - 1])
        return result
