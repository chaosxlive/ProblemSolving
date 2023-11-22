# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        maxLen = 201
        prefix = ""
        for s in strs:
            if len(s) < maxLen:
                maxLen = len(s)
        
        i = 0
        notMatch = False
        while i < maxLen:
            curChar = strs[0][i]
            for s in strs[1:]:
                if s[i] != curChar:
                    notMatch = True
                    break
            if notMatch:
                break
            prefix += curChar
            i += 1
        
        return prefix