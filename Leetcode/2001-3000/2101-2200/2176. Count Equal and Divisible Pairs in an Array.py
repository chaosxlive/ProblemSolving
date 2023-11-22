# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

from typing import List
from collections import defaultdict


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        idxMap = defaultdict(list)
        for idx, num in enumerate(nums):
            idxMap[num].append(idx)
        result = 0
        for idxs in idxMap.values():
            for i in range(len(idxs) - 1):
                for j in range(i + 1, len(idxs)):
                    if (idxs[i] * idxs[j]) % k == 0:
                        result += 1
        return result
