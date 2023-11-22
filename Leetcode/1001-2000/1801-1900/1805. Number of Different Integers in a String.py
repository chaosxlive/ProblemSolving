# https://leetcode.com/problems/number-of-different-integers-in-a-string/

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        numStart = None
        seen = set()
        for index in range(len(word)):
            if '0' <= word[index] <= '9':
                if numStart == None:
                    numStart = index
            elif numStart != None:
                seen.add(int(word[numStart:index]))
                numStart = None
        if numStart != None:
            seen.add(int(word[numStart:]))
            numStart = None

        return len(seen)
