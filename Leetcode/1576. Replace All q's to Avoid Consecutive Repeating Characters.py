# https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

class Solution:
    def modifyString(self, s: str) -> str:
        def getValidChar(index):
            alphabet = [c for c in "abcdefghijklmnopqrstuvwxyz"]
            if index + 1 < len(s) and s[index + 1] in alphabet:
                alphabet.remove(s[index + 1])
            if index - 1 >= 0 and s[index - 1] in alphabet:
                alphabet.remove(s[index - 1])
            return alphabet

        s = [c for c in s]
        for index in range(len(s)):
            if s[index] == '?':
                s[index] = getValidChar(index)[0]
        return "".join(s)
