# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        historyS = {}
        historyT = {}
        for i in range(len(s)):
            if s[i] not in historyS and t[i] not in historyT:
                historyS[s[i]] = t[i]
                historyT[t[i]] = s[i]
            elif s[i] in historyS and t[i] in historyT:
                if historyS[s[i]] != t[i] or historyT[t[i]] != s[i]:
                    return False
            else:
                return False
        return True
