# https://leetcode.com/problems/rotate-function/

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        numSum = sum(nums)
        result = prevTotal = sum([nums[i] * i for i in range(len(nums))])
        for i in range(1, len(nums)):
            prevTotal = prevTotal + numSum - nums[-i] * len(nums)
            result = max(result, prevTotal)
        return result
