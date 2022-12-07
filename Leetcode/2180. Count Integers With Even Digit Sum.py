# https://leetcode.com/problems/count-integers-with-even-digit-sum/

class Solution:
    def countEven(self, num: int) -> int:

        def countNum(n):
            result = 0
            while n > 0:
                result += n % 2
                n //= 10
            return result % 2

        return len([n for n in range(1, num + 1) if countNum(n) == 0])
