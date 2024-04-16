# https://leetcode.com/problems/most-frequent-ids/

from collections import defaultdict
from typing import List

from sortedcontainers import SortedList


class Solution:

    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        result = [0] * len(nums)

        s = SortedList()
        fs = defaultdict(int)

        for i, [n, f] in enumerate(zip(nums, freq)):
            s.discard(fs[n])
            fs[n] += f
            s.add(fs[n])
            result[i] = s[-1]

        return result
