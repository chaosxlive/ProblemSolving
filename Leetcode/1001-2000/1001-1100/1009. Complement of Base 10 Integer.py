# https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        mask = 1
        result = 0
        while True:
            if n & 1 == 0:
                result += mask
            mask <<= 1
            n >>= 1
            if n == 0:
                break
        return result
