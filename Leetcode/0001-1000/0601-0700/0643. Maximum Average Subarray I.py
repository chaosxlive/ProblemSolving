# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        numSum = sum(nums[:k])
        result = numSum / k
        for i in range(k, len(nums)):
            numSum -= nums[i - k]
            numSum += nums[i]
            result = max(result, numSum / k)
        return result
