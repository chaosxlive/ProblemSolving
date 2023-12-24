# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        result = i = firstAIdx = firstBIdx = lastAIdx = lastBIdx = 0
        firstAIdx = i
        i += 1
        while i < len(s):
            if s[i] != s[firstAIdx]:
                break
            i += 1
        lastAIdx = i - 1
        if i == len(s):
            return len(s)
        firstBIdx = i
        lastBIdx = i
        i += 1
        while i < len(s):
            if s[i] == s[firstAIdx]:
                lastAIdx = i
            elif s[i] == s[firstBIdx]:
                lastBIdx = i
            else:
                result = max(result, max(lastAIdx, lastBIdx) - min(firstAIdx, firstBIdx) + 1)
                if lastAIdx > lastBIdx:
                    firstAIdx = lastBIdx + 1
                else:
                    firstAIdx = lastAIdx + 1
                    lastAIdx = lastBIdx
                firstBIdx = i
                lastBIdx = i
            i += 1
        result = max(result,  max(lastAIdx, lastBIdx) - min(firstAIdx, firstBIdx) + 1)
        return result
