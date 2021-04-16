# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alphabet1 = [0] * 26
        alphabet2 = [0] * 26

        for c in s1:
            alphabet1[ord(c) - 97] += 1

        for c in s2[0:len(s1) - 1]:
            alphabet2[ord(c) - 97] += 1

        indexL = 0
        indexR = len(s1) - 1
        while indexR < len(s2):
            alphabet2[ord(s2[indexR]) - 97] += 1
            isMatch = True
            for i in range(26):
                if alphabet1[i] != alphabet2[i]:
                    isMatch = False
                    break
            if isMatch:
                return True
            
            alphabet2[ord(s2[indexL]) - 97] -= 1
            indexL += 1
            indexR += 1
        
        return False
            

