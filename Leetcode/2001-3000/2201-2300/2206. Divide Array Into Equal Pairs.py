# https://leetcode.com/problems/divide-array-into-equal-pairs/

from typing import List
from collections import Counter


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return not any(map(lambda x: x % 2 == 1, Counter(nums).values()))
