# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        index = count = partEnd = farIndex = 0
        while index < len(nums):
            if nums[index] + index > nums[farIndex] + farIndex:
                farIndex = index
            if index == partEnd:
                partEnd = nums[farIndex] + farIndex
                farIndex = index + 1
                count += 1
                if partEnd >= len(nums) - 1:
                    break
            index += 1

        return count
