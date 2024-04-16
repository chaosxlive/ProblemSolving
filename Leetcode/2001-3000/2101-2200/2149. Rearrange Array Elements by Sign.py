# https://leetcode.com/problems/rearrange-array-elements-by-sign/

from typing import List


class Solution:

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posIdx, negIdx = 0, 1
        result = [0] * len(nums)
        for num in nums:
            if num > 0:
                result[posIdx] = num
                posIdx += 2
            else:
                result[negIdx] = num
                negIdx += 2
        return result
