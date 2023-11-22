# https://leetcode.com/problems/count-good-triplets-in-an-array/

from typing import List
from bisect import bisect


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1IdxMap = {}
        for idx, num in enumerate(nums1):
            nums1IdxMap[num] = idx

        nums = [nums1IdxMap[num] for num in nums2]
        incRight = [0] * len(nums)
        arrRight = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            idx = bisect(arrRight, nums[i])
            incRight[i] = len(arrRight) - idx
            arrRight.insert(idx, nums[i])
        incLeft = [0] * len(nums)
        arrLeft = [nums[0]]
        for i in range(1, len(nums)):
            idx = bisect(arrLeft, nums[i])
            incLeft[i] = idx
            arrLeft.insert(idx, nums[i])

        return sum([incLeft[i] * incRight[i] for i in range(1, len(nums) - 1)])
