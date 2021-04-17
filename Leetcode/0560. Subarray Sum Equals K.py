# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        occur_table = {
            0: 1
        }
        result = 0
        currSum = 0
        for num in nums:
            currSum += num
            
            if currSum - k in occur_table:
                result += occur_table[currSum - k]
            
            if currSum in occur_table:
                occur_table[currSum] += 1
            else:
                occur_table[currSum] = 1
        return result
