# https://leetcode.com/contest/weekly-contest-243/problems/check-if-word-equals-summation-of-two-words/

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        num1 = num2 = numT = 0
        for c in firstWord:
            num1 = 10 * num1 + ord(c) - 97
        for c in secondWord:
            num2 = 10 * num2 + ord(c) - 97
        for c in targetWord:
            numT = 10 * numT + ord(c) - 97
        return num1 + num2 == numT
