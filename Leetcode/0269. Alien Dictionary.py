# https://leetcode.com/problems/alien-dictionary/

from typing import List
from collections import defaultdict


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 1:
            return ''.join(set(words[0]))
        chars = set()
        children = defaultdict(list)
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                w1, w2 = words[i], words[j]
                idx = 0
                while idx < len(w1) and idx < len(w2):
                    chars.add(w1[idx])
                    chars.add(w2[idx])
                    if w1[idx] != w2[idx]:
                        if w1[idx] in children[w2[idx]]:
                            return ''
                        children[w1[idx]].append(w2[idx])
                        break
                    idx += 1
                if idx == len(w2) and idx < len(w1):
                    return ''
                for k in range(idx, len(w1)):
                    chars.add(w1[k])
                for k in range(idx, len(w2)):
                    chars.add(w2[k])
        ordered = []
        seen = set()

        def dfs(c):
            for child in children[c]:
                if child not in seen:
                    seen.add(child)
                    dfs(child)
            ordered.append(c)

        for c in chars:
            if c not in seen:
                seen.add(c)
                dfs(c)

        return ''.join(ordered[::-1])
