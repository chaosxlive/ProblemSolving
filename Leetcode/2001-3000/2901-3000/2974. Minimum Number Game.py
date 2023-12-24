# https://leetcode.com/problems/minimum-number-game/

from itertools import chain
from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        return list(chain(*zip(nums[1::2], nums[::2])))
