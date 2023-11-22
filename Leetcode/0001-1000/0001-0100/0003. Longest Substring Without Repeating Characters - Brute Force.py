# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        maxLen = currLen = index = 0
        while index < len(s):
            if s[index] not in chars:
                chars[s[index]] = index
                index += 1
                currLen += 1
            else:
                if currLen > maxLen:
                    maxLen = currLen
                currLen = index - chars[s[index]]
                chars.clear()
                chars[s[index]] = index
                index += 1
        if currLen > maxLen:
            maxLen = currLen

        return maxLen
