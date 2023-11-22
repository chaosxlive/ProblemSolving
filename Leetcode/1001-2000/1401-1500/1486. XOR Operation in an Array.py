# https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = start
        for i in range(1, n):
            result ^= start + 2 * i

        return result
