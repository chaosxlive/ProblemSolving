# https://leetcode.com/problems/3sum-smaller/

from bisect import bisect_left
from typing import List


class Solution:

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        L = len(nums)
        nums.sort()
        res = 0
        for i in range(L - 2):
            for j in range(i + 1, L - 1):
                rest = target - nums[i] - nums[j]
                res += bisect_left(nums, rest, lo=j + 1) - j - 1
        return res
