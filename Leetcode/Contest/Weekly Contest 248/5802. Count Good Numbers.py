# https://leetcode.com/contest/weekly-contest-248/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def fastPow(base, power, mod=1):
            result = 1
            while power > 0:
                if power & 1 != 0:
                    result = (result * base) % mod
                base = (base * base) % mod
                power >>= 1
            return result

        result = fastPow(20, n // 2, 1000000007)
        if n % 2 == 1:
            result *= 5

        return result % 1000000007
