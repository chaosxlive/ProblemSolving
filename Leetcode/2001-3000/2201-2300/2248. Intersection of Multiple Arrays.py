# https://leetcode.com/problems/intersection-of-multiple-arrays/

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result = set(nums[0])
        for i in range(1, len(nums)):
            result.intersection_update(set(nums[i]))
        return sorted(result)
