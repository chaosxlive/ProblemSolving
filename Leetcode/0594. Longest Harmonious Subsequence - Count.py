# https://leetcode.com/problems/longest-harmonious-subsequence/

from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        keys = sorted(counter.keys())
        result = 0
        for i in range(1, len(keys)):
            if abs(keys[i] - keys[i - 1]) == 1:
                result = max(result, counter[keys[i]] + counter[keys[i - 1]])
        return result