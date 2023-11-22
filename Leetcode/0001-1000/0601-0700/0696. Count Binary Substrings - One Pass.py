# https://leetcode.com/problems/count-binary-substrings/

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result, prevCount, currentCount = 0, 0, 1

        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                currentCount += 1
            else:
                result += min(prevCount, currentCount)
                prevCount, currentCount = currentCount, 1

        return result + min(prevCount, currentCount)
