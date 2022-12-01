# https://leetcode.com/problems/best-poker-hand/

from collections import Counter


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return 'Flush'
        m = Counter(ranks).most_common()[0][1]
        if m >= 3:
            return 'Three of a Kind'
        if m == 2:
            return 'Pair'
        return 'High Card'
