# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        target = (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) // 2 if len(nums) % 2 == 0 else nums[len(nums) // 2]
        result = 0
        for num in nums:
            result += target - num if target >= num else num - target
        return result
