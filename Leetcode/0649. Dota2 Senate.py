# https://leetcode.com/problems/dota2-senate/

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qR = deque()
        qD = deque()
        for i, c in enumerate(senate):
            if c == 'R':
                qR.append(i)
            else:
                qD.append(i)
        while len(qR) > 0 and len(qD) > 0:
            r = qR.popleft()
            d = qD.popleft()
            if r < d:
                qR.append(r + len(senate))
            else:
                qD.append(d + len(senate))
        return 'Radiant' if len(qR) > len(qD) else 'Dire'
