# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        seen = set()
        for n in A:
            if n in seen:
                return n
            seen.add(n)