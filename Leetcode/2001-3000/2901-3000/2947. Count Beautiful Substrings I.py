# https://leetcode.com/problems/count-beautiful-substrings-i/

from collections import defaultdict


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        for i in range(1, k+1):
            if i**2 % k == 0:
                minL = i
                break
        vcDiff = 0
        cntV = 0
        result = 0
        cnts = defaultdict(int)
        cnts[(0, 0)] = 1
        for c in s:
            if c in "aeiou":
                vcDiff += 1
                cntV += 1
                cntV %= minL
            else:
                vcDiff -= 1
            result += cnts[(vcDiff, cntV)]
            cnts[(vcDiff, cntV)] += 1
        return result
