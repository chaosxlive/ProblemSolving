# https://leetcode.com/problems/largest-unique-number/

from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        candidates = set()
        seen = set()
        for n in nums:
            if n in seen:
                if n in candidates:
                    candidates.remove(n)
            else:
                seen.add(n)
                candidates.add(n)
        return -1 if len(candidates) == 0 else max(candidates)
