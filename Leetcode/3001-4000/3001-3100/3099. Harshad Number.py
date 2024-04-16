# https://leetcode.com/problems/harshad-number/


class Solution:

    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s, t = 0, x
        while t > 0:
            s += t % 10
            t //= 10
        return s if x % s == 0 else -1
