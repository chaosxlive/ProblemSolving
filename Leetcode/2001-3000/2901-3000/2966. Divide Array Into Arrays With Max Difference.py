# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

from typing import List


class Solution:

    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = [[nums[i], nums[i + 1], nums[i + 2]] for i in range(0, len(nums), 3)]
        for a in result:
            if a[1] - a[0] > k or a[2] - a[0] > k or a[2] - a[1] > k:
                return []
        return result
