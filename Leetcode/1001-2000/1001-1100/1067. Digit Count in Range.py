# https://leetcode.com/problems/digit-count-in-range/


class Solution:

    def digitsCount(self, d: int, low: int, high: int) -> int:

        def calc(n):
            result = 0
            i = 1
            while i <= n:
                left = n // i
                right = n % i
                result += (left + 9 - d) // 10 * i + ((right + 1) if left % 10 == d else 0)
                if d == 0:
                    result -= i
                i *= 10
            return result

        return calc(high) - calc(low - 1)
