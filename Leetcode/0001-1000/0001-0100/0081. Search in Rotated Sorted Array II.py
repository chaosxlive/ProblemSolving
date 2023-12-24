# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums
