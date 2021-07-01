# https://leetcode.com/problems/maximum-alternating-subsequence-sum/

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        maxNum = positive = negative = 0
        for num in nums:
            temp1 = max(positive, negative + num, num)
            temp2 = max(negative, positive - num, 0)
            positive = temp1
            negative = temp2
            maxNum = max(maxNum, positive, negative)
        return maxNum
