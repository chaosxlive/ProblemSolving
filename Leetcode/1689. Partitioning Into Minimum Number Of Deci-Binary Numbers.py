# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution:
    def minPartitions(self, n: str) -> int:
        result = 0
        for c in n:
            if ord(c) > result:
                result = ord(c)
        return result - 48
