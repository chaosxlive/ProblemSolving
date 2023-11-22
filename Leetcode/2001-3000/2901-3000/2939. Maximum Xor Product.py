class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        for i in reversed(range(n)):
            bit = 1 << i
            if a & bit > 0 and b & bit > 0:
                pass
            elif a & bit > 0:
                if a > b:
                    a ^= bit
                    b |= bit
            elif b & bit > 0:
                if b > a:
                    b ^= bit
                    a |= bit
            else:
                a |= bit
                b |= bit
        return ((a % MOD) * (b % MOD)) % MOD
