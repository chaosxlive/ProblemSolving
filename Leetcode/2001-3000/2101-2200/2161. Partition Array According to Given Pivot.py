# https://leetcode.com/problems/partition-array-according-to-given-pivot/

from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        cnt = 0
        right = []
        for num in nums:
            if num > pivot:
                right.append(num)
            elif num < pivot:
                left.append(num)
            else:
                cnt += 1
        return left + ([pivot] * cnt) + right
