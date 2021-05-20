# https://leetcode.com/problems/ugly-number-iii/

from math import gcd


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def lcm(a, b, c=1):
            temp = a * b // gcd(a, b)
            return temp * c // gcd(temp, c)

        def countUgly(n, a, b, c):
            test = n // a + n // b + n // c \
                - n // lcm(a, b) - n // lcm(a, c) - n // lcm(b, c) \
                + n // lcm(a, b, c)
            return n // a + n // b + n // c \
                - n // lcm(a, b) - n // lcm(a, c) - n // lcm(b, c) \
                + n // lcm(a, b, c)

        lower, upper = 1, 2000000001
        while True:
            center = (lower + upper) // 2
            count = countUgly(center, a, b, c)
            if count == n and lower + 1 >= upper:
                return center
            elif count < n:
                lower = center + 1
            elif count >= n:
                upper = center
