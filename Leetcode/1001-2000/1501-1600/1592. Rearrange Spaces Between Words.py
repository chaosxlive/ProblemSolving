# https://leetcode.com/problems/rearrange-spaces-between-words/

class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = list(filter(lambda s: len(s) > 0, text.split(' ')))
        spaces = text.count(' ')
        if spaces == 0:
            return text
        if len(words) == 1:
            return words[0] + ' ' * spaces
        return (' ' * (spaces // (len(words) - 1))).join(words) + ' ' * (spaces % (len(words) - 1))
