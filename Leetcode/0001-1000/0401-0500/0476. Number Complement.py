# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        result = 0
        while True:
            if num & 1 == 0:
                result += mask
            mask <<= 1
            num >>= 1
            if num == 0:
                break
        return result
