# https://leetcode.com/problems/synonymous-sentences/

from typing import List
from collections import defaultdict


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        uf = {}
        wordSet = set()

        def find(x):
            if x not in uf:
                uf[x] = x
            elif uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                uf[rx] = ry

        for x, y in synonyms:
            wordSet.add(x)
            wordSet.add(y)
            union(x, y)

        synonymMap = defaultdict(list)
        for word in wordSet:
            synonymMap[find(word)].append(word)

        words = text.split(' ')
        result = []

        def dfs(path: List[str], idx: int):
            if idx == len(words):
                result.append(' '.join(path))
                return
            if len(synonymMap[find(words[idx])]) == 0:
                path.append(words[idx])
                dfs(path, idx + 1)
                path.pop()
            else:
                for synonym in sorted(synonymMap[find(words[idx])]):
                    path.append(synonym)
                    dfs(path, idx + 1)
                    path.pop()

        dfs([], 0)

        return result
