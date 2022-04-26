# https://leetcode.com/problems/maximum-difference-between-increasing-elements/

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minNum = nums[0]
        result = -1
        for i in range(1, len(nums)):
            if nums[i] > minNum:
                result = max(result, nums[i] - minNum)
            else:
                minNum = min(minNum, nums[i])
        return result
