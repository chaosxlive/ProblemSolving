# https://leetcode.com/contest/weekly-contest-254/problems/minimum-non-zero-product-of-the-array-elements/

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p == 1:
            return 1

        def fastPow(base, power, mod=1):
            result = 1
            while power > 0:
                if power & 1 != 0:
                    result = (result * base) % mod
                base = (base * base) % mod
                power >>= 1
            return result

        return ((2 ** p) - 1) * fastPow((2 ** p) - 2, (2 ** (p - 1)) - 1, 1000000007) % 1000000007
