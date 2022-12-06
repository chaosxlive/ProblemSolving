# https://leetcode.com/problems/degree-of-an-array/

from typing import List
from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        seen = defaultdict(lambda: [50001, -1])
        cnt = defaultdict(lambda: [0, -1])
        for idx, num in enumerate(nums):
            seen[num] = [min(seen[num][0], idx), idx]
            cnt[num] = [cnt[num][0] + 1, num]
        cnt = sorted(cnt.values(), reverse=True)
        result = 50001
        for [c, n] in cnt:
            if c != cnt[0][0]:
                break
            result = min(result, seen[n][1] - seen[n][0] + 1)
        return result
