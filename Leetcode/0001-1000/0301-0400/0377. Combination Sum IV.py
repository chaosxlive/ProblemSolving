# https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [1]

        for i in range(1, target + 1):
            tempSum = 0
            for num in nums:
                if num > i:
                    break
                tempSum += dp[i - num]
            dp.append(tempSum)
        
        return dp[target]