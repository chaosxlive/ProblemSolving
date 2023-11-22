# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        leftMax = rightMax = 0
        while left < right:
            if height[left] >= height[right]:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    result += rightMax - height[right]
                right -= 1
            else:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    result += leftMax - height[left]
                left += 1
        return result
