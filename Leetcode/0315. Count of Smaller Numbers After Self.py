# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        seen = SortedList()
        result = [0] * len(nums)
        for index in range(len(nums) - 1, -1, -1):
            result[index] = seen.bisect_left(nums[index])
            seen.add(nums[index])
        return result
