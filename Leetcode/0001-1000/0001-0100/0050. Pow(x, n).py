# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x

        half = self.myPow(x, abs(n) // 2)
        result = half * half * (1 if n % 2 == 0 else x)
        return (1 / result) if n < 0 else result
