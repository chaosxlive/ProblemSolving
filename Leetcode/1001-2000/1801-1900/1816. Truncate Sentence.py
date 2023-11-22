# https://leetcode.com/problems/truncate-sentence/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        countWord = 0
        for i in range(len(s)):
            if s[i] == ' ':
                countWord += 1
                if countWord == k:
                    return s[:i]
        return s
