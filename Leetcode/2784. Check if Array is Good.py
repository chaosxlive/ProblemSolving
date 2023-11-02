# https://leetcode.com/problems/check-if-array-is-good/

from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()
        arr = [i for i in range(1, n)] + [n - 1]
        for i in range(n):
            if nums[i] != arr[i]:
                return False
        return True
