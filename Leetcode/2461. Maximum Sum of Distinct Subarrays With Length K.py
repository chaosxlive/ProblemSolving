# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(lambda: 0)
        invalidCnt = 0
        numSum = 0
        result = 0
        for i in range(k):
            num = nums[i]
            if seen[num] > 0:
                invalidCnt += 1
            seen[num] += 1
            numSum += num
        if invalidCnt == 0:
            result = numSum
        for i in range(k, len(nums)):
            prevNum = nums[i - k]
            if seen[prevNum] > 1:
                invalidCnt -= 1
            seen[prevNum] -= 1
            numSum -= prevNum
            num = nums[i]
            if seen[num] > 0:
                invalidCnt += 1
            seen[num] += 1
            numSum += num
            if invalidCnt == 0:
                result = max(result, numSum)
        return result
