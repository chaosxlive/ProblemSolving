# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        zeroIdx = 0

        def calcMaxLength(nums: List[int], left: int, right: int) -> int:
            if left >= right:
                return 0
            length = right - left
            negativeCnt = len(list(filter(lambda x: x < 0, nums[left:right])))
            if negativeCnt & 1 == 0:
                return length
            result = 0
            for i in range(left, right):
                if nums[i] < 0:
                    result = max(result, i - left, right - i - 1)
            return result

        result = 0
        prevNonZeroIdx = 0
        try:
            while True:
                zeroIdx = nums.index(0, zeroIdx)
                result = max(result, calcMaxLength(nums, prevNonZeroIdx, zeroIdx))
                zeroIdx += 1
                prevNonZeroIdx = zeroIdx
        except:
            result = max(result, calcMaxLength(nums, prevNonZeroIdx, len(nums)))
        return result
