from typing import List


class Solution:

    def minimumArrayLength(self, nums: List[int]) -> int:
        nums.sort()
        mc = nums.count(nums[0])
        if mc == 1:
            return 1

        for i in range(1, len(nums)):
            md = nums[i] % nums[0]
            if md != 0:
                return 1
        return (mc + 1) // 2
