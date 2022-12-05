# https://leetcode.com/problems/minimum-average-difference/

from itertools import accumulate


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefixSum = list(accumulate(nums))
        resultVal = prefixSum[-1] // len(nums)
        resultIdx = len(nums) - 1
        for i in range(len(nums) - 1):
            avg = abs((prefixSum[i] // (i + 1)) - ((prefixSum[-1] - prefixSum[i]) // (len(nums) - i - 1)))
            if avg < resultVal:
                resultVal = avg
                resultIdx = i
            elif avg == resultVal and i < resultIdx:
                resultIdx = i
        return resultIdx
