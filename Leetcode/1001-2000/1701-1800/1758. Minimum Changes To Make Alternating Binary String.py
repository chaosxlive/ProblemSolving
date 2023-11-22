# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution:
    def minOperations(self, s: str) -> int:
        diff0 = diff1 = 0
        for i, c in enumerate(s):
            if str(i % 2) != c:
                diff0 += 1
            else:
                diff1 += 1

        return min(diff0, diff1)
