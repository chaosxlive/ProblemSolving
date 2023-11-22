# https://leetcode.com/problems/broken-calculator/

class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        count = 0
        while y > x:
            if y % 2 == 0:
                y //= 2
            else:
                y += 1
            count += 1
        return count + x - y
