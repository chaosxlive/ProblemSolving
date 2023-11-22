# https://leetcode.com/problems/buddy-strings/

class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        countChar = {}
        isSameChar = False
        for c in a:
            if c not in countChar:
                countChar[c] = 0
            else:
                isSameChar = True
            countChar[c] += 1
        for c in b:
            if c not in countChar:
                return False
            countChar[c] -= 1
        for val in countChar.values():
            if val != 0:
                return False

        countDiff = 0
        for index in range(len(a)):
            if a[index] != b[index]:
                countDiff += 1

        return countDiff == 2 or (countDiff == 0 and isSameChar)
