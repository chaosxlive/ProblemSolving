# https://leetcode.com/problems/longest-harmonious-subsequence/

from collections import defaultdict


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        result = 0
        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1
            if num - 1 in seen:
                result = max(result, seen[num - 1] + seen[num])
            if num + 1 in seen:
                result = max(result, seen[num] + seen[num + 1])
        return result
