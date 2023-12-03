# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        i = 0
        num = 1
        while num * 2 <= n:
            num *= 2
            i += 1
        return (2 ** (i + 1)) - 1 - self.minimumOneBitOperations(n ^ num)
