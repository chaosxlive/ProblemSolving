# https://leetcode.com/problems/reverse-words-in-a-string/description/

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(list(filter(lambda x: len(x) > 0, s.split(' ')))))
