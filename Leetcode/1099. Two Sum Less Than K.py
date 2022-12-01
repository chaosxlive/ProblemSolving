# https://leetcode.com/problems/two-sum-less-than-k/

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        length = len(nums)
        result = -1
        for i in range(length - 1):
            for j in range(i + 1, length):
                s = nums[i] + nums[j]
                if s < k:
                    result = max(result, s)
        return result
