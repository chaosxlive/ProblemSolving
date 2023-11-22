# https://leetcode.com/problems/shortest-word-distance-iii/

from typing import List


class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        mark = []
        idxs = []
        isSame = word1 == word2
        for idx, word in enumerate(wordsDict):
            if word == word1:
                mark.append(1)
                idxs.append(idx)
            elif word == word2:
                mark.append(2)
                idxs.append(idx)
        result = 2147483647
        for i in range(len(mark) - 1):
            if isSame:
                result = min(result, abs(idxs[i] - idxs[i + 1]))
            elif mark[i] != mark[i + 1]:
                result = min(result, abs(idxs[i] - idxs[i + 1]))
        return result
