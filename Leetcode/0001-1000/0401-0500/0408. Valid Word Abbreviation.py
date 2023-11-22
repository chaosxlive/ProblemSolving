# https://leetcode.com/problems/valid-word-abbreviation/

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        ptrW = ptrA = 0
        while ptrW < len(word) and ptrA < len(abbr):
            if word[ptrW] == abbr[ptrA]:
                ptrW += 1
                ptrA += 1
            elif abbr[ptrA].isalpha():
                return False
            else:
                if abbr[ptrA] == '0':
                    return False
                n = 0
                while ptrA < len(abbr) and abbr[ptrA].isdigit():
                    n = n * 10 + int(abbr[ptrA])
                    ptrA += 1
                ptrW += n
        return ptrW == len(word) and ptrA == len(abbr)
