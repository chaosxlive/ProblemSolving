# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        countChar = {}
        for c in s1:
            if c not in countChar:
                countChar[c] = 0
            countChar[c] += 1
        for c in s2:
            if c not in countChar:
                return False
            countChar[c] -= 1
        for val in countChar.values():
            if val != 0:
                return False

        countDiff = 0
        for index in range(len(s1)):
            if s1[index] != s2[index]:
                countDiff += 1
        return countDiff == 0 or countDiff == 2
