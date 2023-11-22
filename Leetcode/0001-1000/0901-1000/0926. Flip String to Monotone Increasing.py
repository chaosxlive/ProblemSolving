# https://leetcode.com/problems/flip-string-to-monotone-increasing/

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        prefix = [0] * (len(s) + 1)
        for i in range(len(s)):
            prefix[i + 1] = prefix[i] + 1 if s[i] == '1' else prefix[i]
        return min(2 * prefix[i] + len(s) - i - prefix[-1] for i in range(len(prefix)))
