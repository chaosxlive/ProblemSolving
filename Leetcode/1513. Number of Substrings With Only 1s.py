# https://leetcode.com/problems/number-of-substrings-with-only-1s/

class Solution:
    def numSub(self, s: str) -> int:
        return sum((lambda x: (len(x) * (len(x) + 1) // 2) % 1000000007)(x) for x in s.split('0')) % 1000000007
