# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = len(nums) - 2
        while index >= 0 and nums[index + 1] <= nums[index]:
            index -= 1
        if index >= 0:
            indexSwap = len(nums) - 1
            while indexSwap >= 0 and nums[indexSwap] <= nums[index]:
                indexSwap -= 1
            nums[index], nums[indexSwap] = nums[indexSwap], nums[index]
        i, j = index + 1, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
