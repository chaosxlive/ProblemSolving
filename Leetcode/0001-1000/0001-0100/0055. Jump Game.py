# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        index, target = len(nums) - 2, len(nums) - 1
        while index >= 0:
            if nums[index] + index >= target:
                target = index
                if target == 0:
                    return True
            index -= 1
        return False
