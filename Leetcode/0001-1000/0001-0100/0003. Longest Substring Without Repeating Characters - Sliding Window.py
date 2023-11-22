# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = maxLen = 0
        chars = {}

        while right < len(s):
            if s[right] in chars:
                left = max(left, chars[s[right]] + 1)
            maxLen = max(maxLen, right - left + 1)
            chars[s[right]] = right
            right += 1

        return maxLen
