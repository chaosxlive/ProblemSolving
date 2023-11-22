# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = [0] * len(nums)
        total = 0
        for i in range(len(nums)):
            leftSum[i] = total
            total += nums[i]

        for i in range(len(nums)):
            if total - nums[i] - leftSum[i] == leftSum[i]:
                return i
        return -1
