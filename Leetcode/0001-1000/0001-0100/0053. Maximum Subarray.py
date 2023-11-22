# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # https://en.wikipedia.org/wiki/Maximum_subarray_problem

        result = currentMax = nums[0]
        for num in nums[1:]:
            currentMax = max(num, currentMax + num)
            result = max(result, currentMax)
        return result
