# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        index = 0
        for word in words:
            if s[index:index + len(word)] == word:
                index += len(word)
            else:
                return False
            if index == len(s):
                return True
