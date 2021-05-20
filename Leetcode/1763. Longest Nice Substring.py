# https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        countUpper, countLower = set(), set()
        maxStr = ""
        maxCount = 0
        for left in range(len(s)):
            countLower.clear()
            countUpper.clear()
            for right in range(left, len(s)):
                if 'a' <= s[right] <= 'z':
                    countLower.add(s[right])
                else:
                    countUpper.add(s[right])

                if len(countLower) == len(countUpper) and maxCount < right - left + 1:
                    isMatch = True
                    for lower in countLower:
                        if lower.upper() not in countUpper:
                            isMatch = False
                            break
                    if isMatch:
                        for upper in countUpper:
                            if upper.lower() not in countLower:
                                isMatch = False
                                break
                    if isMatch:
                        maxStr = s[left:right + 1]
                        maxCount = right - left + 1
        return maxStr
