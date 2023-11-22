# https://leetcode.com/problems/find-champion-ii/

from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        isChamp = {i: True for i in range(n)}
        for _, b in edges:
            isChamp[b] = False
        win = -1
        for i in range(n):
            if isChamp[i]:
                if win == -1:
                    win = i
                else:
                    return -1
        return win
