# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

class Solution:
    def minFlips(self, s: str) -> int:
        l = len(s)
        s += s

        g1 = '10' * l
        g2 = '01' * l

        diff1 = [0] * (2 * l + 1)
        diff2 = [0] * (2 * l + 1)

        for i in range(2 * l):
            if s[i] != g1[i]:
                diff1[i + 1] = diff1[i] + 1
            else:
                diff1[i + 1] = diff1[i]
            if s[i] != g2[i]:
                diff2[i + 1] = diff2[i] + 1
            else:
                diff2[i + 1] = diff2[i]

        result = l
        for i in range(l):
            result = min(result, diff1[i + l] - diff1[i], diff2[i + l] - diff2[i])
        return result
