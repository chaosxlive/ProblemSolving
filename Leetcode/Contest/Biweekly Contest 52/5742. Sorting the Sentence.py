# https://leetcode.com/contest/biweekly-contest-52/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        reWords = [0] * len(words)
        for word in words:
            reWords[int(word[-1]) - 1] = word[:-1]
        return " ".join(reWords)