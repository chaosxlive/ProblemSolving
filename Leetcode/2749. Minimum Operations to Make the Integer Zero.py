# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(0, 61):
            left = num1 - k * num2
            if left < 0 or left < k:
                continue
            rightBits = 0
            right = left
            while right > 0:
                rightBits += right & 1
                right >>= 1
            if rightBits <= k:
                return k
        return -1