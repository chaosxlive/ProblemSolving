# https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        i = 0
        result = []

        while i < len(nums):
            result.insert(index[i], nums[i])
            i += 1

        return result