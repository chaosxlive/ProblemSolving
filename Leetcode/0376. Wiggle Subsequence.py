# https://leetcode.com/problems/wiggle-subsequence/

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        picked = nums[:1]
        isFindingBigger = True
        for i in range(1, len(nums)):
            if isFindingBigger:
                if nums[i] <= picked[-1]:
                    picked[-1] = nums[i]
                else:
                    picked.append(nums[i])
                    isFindingBigger = False
            else:
                if nums[i] >= picked[-1]:
                    picked[-1] = nums[i]
                else:
                    picked.append(nums[i])
                    isFindingBigger = True
        result = len(picked)
        picked = nums[:1]
        isFindingBigger = False
        for i in range(1, len(nums)):
            if isFindingBigger:
                if nums[i] <= picked[-1]:
                    picked[-1] = nums[i]
                else:
                    picked.append(nums[i])
                    isFindingBigger = False
            else:
                if nums[i] >= picked[-1]:
                    picked[-1] = nums[i]
                else:
                    picked.append(nums[i])
                    isFindingBigger = True
        return max(result, len(picked))
