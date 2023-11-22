# https://leetcode.com/problems/alternating-digit-sum/

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        result = 0
        isPositive = False
        while n > 0:
            if isPositive:
                result -= n % 10
            else:
                result += n % 10
            n //= 10
            isPositive = not isPositive
        return result if isPositive else -result
