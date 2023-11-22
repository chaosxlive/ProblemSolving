# https://leetcode.com/problems/min-max-game/

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return self.minMaxGame([min(nums[2 * i], nums[2 * i + 1]) if i % 2 == 0 else max(nums[2 * i], nums[2 * i + 1]) for i in range(len(nums) // 2)])
