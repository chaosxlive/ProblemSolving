# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26

        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        result = -1

        for i in range(26):
            if first[i] != -1 and last[i] != -1:
                result = max(result, last[i] - first[i] - 1)

        return result
