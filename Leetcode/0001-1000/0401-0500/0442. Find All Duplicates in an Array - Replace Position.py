# https://leetcode.com/problems/find-all-duplicates-in-an-array/

from typing import List


class Solution:

    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = set()
        i = 0
        L = len(nums)
        while i < L:
            if nums[i] == i + 1:
                i += 1
                continue
            j = nums[i] - 1
            if nums[i] == nums[j]:
                res.add(nums[i])
                i += 1
                continue
            nums[i], nums[j] = nums[j], nums[i]
        return list(res)
