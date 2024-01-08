# https://leetcode.com/problems/one-edit-distance/

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == '' and t == '':
            return False
        LS = len(s)
        LT = len(t)
        LD = abs(LS - LT)
        if LD > 1:
            return False
        elif LD == 1 and (s == '' or t == ''):
            return True
        if LS - LT == 1:
            s, t = t, s
            LS, LT = LT, LS
        if LD == 1:
            si = ti = 0
            isAdded = False
            while si < LS:
                if s[si] == t[ti]:
                    si += 1
                    ti += 1
                else:
                    if isAdded:
                        return False
                    ti += 1
                    isAdded = True
            if not isAdded:
                return ti < LT
            return True
        else:
            isChanged = False
            for i in range(LS):
                if s[i] != t[i]:
                    if isChanged:
                        return False
                    else:
                        isChanged = True
            return isChanged
