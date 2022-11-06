# https://leetcode.com/problems/hand-of-straights/

from collections import Counter


class Solution:
    def isNStraightHand(self, hand, groupSize: int) -> bool:
        if groupSize == 1:
            return True
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        cs = sorted(map(lambda x: list(x), counter.items()), key=lambda x: x[0])
        for csi in range(len(cs)):
            n = cs[csi][1]
            if n == 0:
                continue
            for i in range(groupSize):
                if csi + i >= len(cs) or cs[csi + i][0] != cs[csi][0] + i or cs[csi + i][1] < n:
                    return False
                cs[csi + i][1] -= n
        return True
