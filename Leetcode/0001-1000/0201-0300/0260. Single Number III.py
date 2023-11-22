# https://leetcode.com/problems/single-number-iii/

from typing import List
from functools import reduce
from operator import xor


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        allXor = reduce(xor, nums, 0)
        mask = allXor & (~allXor + 1)
        a = reduce(xor, filter(lambda x: x & mask > 0, nums), 0)
        return [a, allXor ^ a]
