# https://leetcode.com/problems/number-of-longest-increasing-subsequence/

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        resultMaxLen = 1
        resultCnt = 0
        maxLen = [1] * len(nums)
        cnt = [1] * len(nums)
        for right in range(len(nums)):
            for left in range(right):
                if nums[right] > nums[left]:
                    if maxLen[left] + 1 > maxLen[right]:
                        maxLen[right] = maxLen[left] + 1
                        cnt[right] = cnt[left]
                    elif maxLen[left] + 1 == maxLen[right]:
                        cnt[right] += cnt[left]
            if maxLen[right] > resultMaxLen:
                resultMaxLen = maxLen[right]
                resultCnt = cnt[right]
            elif maxLen[right] == resultMaxLen:
                resultCnt += cnt[right]
        return resultCnt
