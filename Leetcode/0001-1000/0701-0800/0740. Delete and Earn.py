# https://leetcode.com/problems/delete-and-earn/

from typing import List
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = sorted(Counter(nums).items())
        prev = [-1, 0, 0]  # Num, Take, Skip
        for num, cnt in counts:
            prev = [num, (prev[2] if num == prev[0] + 1 else max(prev[1], prev[2])) + num * cnt, max(prev[1], prev[2])]
        return max(prev[1], prev[2])
