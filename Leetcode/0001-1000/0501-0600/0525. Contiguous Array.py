# https://leetcode.com/problems/contiguous-array/

from typing import List


class Solution:

    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0: -1}
        result = 0
        s = 0
        for i, n in enumerate(nums):
            s += 1 if n == 1 else -1
            if s in seen:
                result = max(result, i - seen[s])
            else:
                seen[s] = i
        return result