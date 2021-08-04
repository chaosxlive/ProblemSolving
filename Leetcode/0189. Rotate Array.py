# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        def reverse(nums, start, end):
            indexLeft, indexRight = start, end - 1
            while indexLeft < indexRight:
                nums[indexLeft], nums[indexRight] = nums[indexRight], nums[indexLeft]
                indexLeft += 1
                indexRight -= 1
        
        reverse(nums, 0, len(nums))
        reverse(nums, 0, k)
        reverse(nums, k, len(nums))