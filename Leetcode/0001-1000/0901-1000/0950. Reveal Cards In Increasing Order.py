# https://leetcode.com/problems/reveal-cards-in-increasing-order/

from collections import deque
from typing import List


class Solution:

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = deque(range(len(deck)))
        idxs = []
        while q:
            idxs.append(q.popleft())
            q.rotate(-1)
        deck.sort()
        res = [0] * len(deck)
        for i, j in enumerate(idxs):
            res[j] = deck[i]
        return res
