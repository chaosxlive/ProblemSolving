
class Solution:

    def minEnd(self, n: int, x: int) -> int:
        res = x
        N = n - 1
        resBit = 0
        cnt = 1
        nBit = 0
        while res & (1 << resBit) > 0:
            resBit += 1
        while cnt - 1 <= N:
            if res & (1 << resBit) == 0:
                if N & (1 << nBit) > 0:
                    res |= 1 << resBit
                nBit += 1
                cnt <<= 1
            resBit += 1
        return res


# print(Solution().minEnd(3, 4))
# print(Solution().minEnd(2, 7))
