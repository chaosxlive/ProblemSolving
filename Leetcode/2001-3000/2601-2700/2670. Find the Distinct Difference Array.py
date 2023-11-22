# https://leetcode.com/problems/find-the-distinct-difference-array/

from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        return list(len(set(nums[:i + 1])) - len(set(nums[i + 1:])) for i in range(len(nums)))
