# https://leetcode.com/problems/longest-subsequence-with-limited-sum/

import bisect


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        result = []
        for q in queries:
            result.append(bisect.bisect(nums, q))
        return result
