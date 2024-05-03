# https://leetcode.com/problems/count-pairs-in-two-arrays/

from typing import List


class Solution:

    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        diffs = sorted(map(lambda x: x[0] - x[1], zip(nums1, nums2)))
        res = 0
        left = 0
        right = len(diffs) - 1
        while left < right:
            if diffs[left] + diffs[right] > 0:
                res += right - left
                right -= 1
            else:
                left += 1
        return res
