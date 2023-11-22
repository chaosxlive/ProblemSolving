# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x ^ y
        result = 0
        while temp > 0:
            if temp & 1 == 1:
                result += 1
            temp >>= 1
        return result
