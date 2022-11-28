# https://leetcode.com/problems/convert-to-base-2/

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        digits = []
        while n != 0:
            n, remainder = divmod(n, -2)
            if remainder < 0:
                n, remainder = n + 1, remainder + 2
            digits.append(str(remainder))
        return "".join(digits[::-1])
