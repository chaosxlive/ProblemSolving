# https://leetcode.com/problems/binary-gap/

class Solution:
    def binaryGap(self, n: int) -> int:
        distStr = bin(n)[2:].split('1')[1:-1]
        return 0 if len(distStr) == 0 else max(map(lambda x: len(x), distStr)) + 1
