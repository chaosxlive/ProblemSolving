# https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

MOD = 1000000007


class Solution:
    def stringCount(self, n: int) -> int:
        # Start with any choice
        result = pow(26, n, MOD)

        # no L
        result -= pow(25, n, MOD)
        # no T
        result -= pow(25, n, MOD)
        # no E
        result -= pow(25, n, MOD)
        # only 1 E
        result -= n * pow(25, n - 1, MOD)

        # no L and no T
        result += pow(24, n, MOD)
        # no L and no E
        result += pow(24, n, MOD)
        # no L and only 1 E
        result += n * pow(24, n - 1, MOD)
        # no T and no E
        result += pow(24, n, MOD)
        # no T and only 1 E
        result += n * pow(24, n - 1, MOD)

        # no L and no T and no E
        result -= pow(23, n, MOD)
        # no L and no T and one E
        result -= n * pow(23, n - 1, MOD)

        return (result + MOD) % MOD
