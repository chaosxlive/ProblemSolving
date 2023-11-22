# https://leetcode.com/problems/elimination-game/

class Solution:
    def lastRemaining(self, n: int) -> int:
        left, right, mask, isLeft = 1, n, 1, True
        while left < right:
            if isLeft:
                if (left & mask > 0 and right & mask > 0) or \
                        (left & mask == 0 and right & mask == 0):
                    right -= mask
                left += mask
            else:
                if (right & mask > 0 and left & mask > 0) or \
                        (right & mask == 0 and left & mask == 0):
                    left += mask
                right -= mask
            isLeft = not isLeft
            mask <<= 1
        return left
