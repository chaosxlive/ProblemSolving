# https://leetcode.com/problems/odd-string-difference/

from collections import defaultdict


class Solution:
    def oddString(self, words: List[str]) -> str:
        history = defaultdict(lambda: [])
        for word in words:
            arr = []
            for i in range(len(word) - 1):
                arr.append(ord(word[i + 1]) - ord(word[i]))
            history[tuple(arr)].append(word)
        for val in history.values():
            if len(val) == 1:
                return val[0]
        return ''
