# https://leetcode.com/problems/count-distinct-numbers-on-board/

class Solution:
    def distinctIntegers(self, n: int) -> int:
        return max(n - 1, 1)
