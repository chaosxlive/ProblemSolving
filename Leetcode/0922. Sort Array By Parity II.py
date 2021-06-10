# https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1
        while True:
            while even < len(nums) and nums[even] % 2 == 0:
                even += 2
            while odd < len(nums) and nums[odd] % 2 == 1:
                odd += 2
            if even >= len(nums) or odd >= len(nums):
                return nums
            nums[even], nums[odd] = nums[odd], nums[even]
