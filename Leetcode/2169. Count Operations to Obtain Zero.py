# https://leetcode.com/problems/count-operations-to-obtain-zero/

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0
        result = 0
        large, small = max(num1, num2), min(num1, num2)
        result += large // small
        large %= small
        if large != 0 and small != 0:
            result += self.countOperations(large, small)
        return result
