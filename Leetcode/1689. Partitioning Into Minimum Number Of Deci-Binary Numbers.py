# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution:
    def minPartitions(self, n: str) -> int:
        result = 0
        for c in n:
            if ord(c) - 48 > result:
                result = ord(c) - 48
        return result