# https://leetcode.com/problems/subarray-sums-divisible-by-k/

from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        current = 0
        counter = defaultdict(int)
        counter[0] += 1
        for num in nums:
            current += num
            current %= k
            counter[current] += 1
        return sum(v * (v - 1) // 2 for v in counter.values() if v > 1)
