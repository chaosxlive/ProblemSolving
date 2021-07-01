# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if divisor == 1:
            return dividend
        isNeg = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0

        while divisor <= dividend:
            tempDivisor = divisor
            tempResult = 1
            while (tempDivisor << 1) <= dividend:
                tempDivisor <<= 1
                tempResult <<= 1
            dividend -= tempDivisor
            result += tempResult

        return -result if isNeg else result
