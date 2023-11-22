# https://leetcode.com/problems/uncommon-words-from-two-sentences/

from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [word for word, count in Counter(s1.split(' ') + s2.split(' ')).items() if count == 1]
