# https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

from typing import List


class Solution:

    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for i in range(2, len(nums)):
            num = nums[i]
            if arr1[-1] > arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)
        return arr1 + arr2
