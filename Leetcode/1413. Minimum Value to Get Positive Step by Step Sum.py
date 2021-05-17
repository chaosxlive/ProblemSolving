# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minSum = curSum = 0
        for num in nums:
            curSum += num
            if curSum < minSum:
                minSum = curSum
        
        return -minSum + 1 if minSum <= 0 else 1