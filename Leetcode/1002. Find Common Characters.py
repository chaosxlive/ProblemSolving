# https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = {c: ([0] * len(words)) for c in "abcdefghijklmnopqrstuvwxyz"}
        for i, word in enumerate(words):
            for c in word:
                counts[c][i] += 1
        return [c for c in "abcdefghijklmnopqrstuvwxyz" for times in range(min(counts[c]))]
