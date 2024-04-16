from collections import Counter
from typing import List, Optional


class Solution:

    def isPossibleToSplit(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for v in c.values():
            if v > 2:
                return False
        return True
