# https://leetcode.com/problems/maximum-ascending-subarray-sum/

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curSum = nums[0]
        maxSum = nums[0]
        for index in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                curSum += nums[index]
            else:
                if curSum > maxSum:
                    maxSum = curSum
                curSum = nums[index]
            index += 1
        if curSum > maxSum:
            maxSum = curSum

        return maxSum
