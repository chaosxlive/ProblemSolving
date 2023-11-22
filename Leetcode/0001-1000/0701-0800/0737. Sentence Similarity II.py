# https://leetcode.com/problems/sentence-similarity-ii/

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        uf = {}

        def find(w):
            if w not in uf:
                uf[w] = w
            elif w != uf[w]:
                uf[w] = find(uf[w])
            return uf[w]

        def union(w1, w2):
            r1, r2 = find(w1), find(w2)
            if r1 != r2:
                uf[r1] = r2

        for [a, b] in similarPairs:
            union(a, b)

        for i in range(len(sentence1)):
            if find(sentence1[i]) != find(sentence2[i]):
                return False
        return True
