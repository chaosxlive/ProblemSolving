# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = white = blue = 0
        for color in nums:
            if color == 0:
                red += 1
            elif color == 1:
                white += 1
            else:
                blue += 1
        index = 0
        while red > 0:
            nums[index] = 0
            red -= 1
            index += 1
        while white > 0:
            nums[index] = 1
            white -= 1
            index += 1
        while blue > 0:
            nums[index] = 2
            blue -= 1
            index += 1
