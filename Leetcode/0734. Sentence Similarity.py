# https://leetcode.com/problems/sentence-similarity/

from collections import defaultdict


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        sMap = defaultdict(set)
        for [a, b] in similarPairs:
            sMap[a].add(b)
            sMap[b].add(a)

        for i in range(len(sentence1)):
            if sentence1[i] != sentence2[i] and sentence1[i] not in sMap[sentence2[i]]:
                return False
        return True
