# https://leetcode.com/problems/shortest-completing-word/

from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        target = Counter(c for c in licensePlate.lower() if 'a' <= c <= 'z')
        result = "z" * 1000
        for word in words:
            isValid = True
            count = Counter(c for c in word.lower() if 'a' <= c <= 'z')
            for key in target.keys():
                if count[key] < target[key]:
                    isValid = False
                    break
            if isValid:
                if len(word) < len(result):
                    result = word
        return result
