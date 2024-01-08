# https://leetcode.com/problems/integer-replacement/

from collections import deque


class Solution:
    def integerReplacement(self, n: int) -> int:
        dq = deque([(n, 0)])
        seen = set([n])
        while True:
            v, s = dq.popleft()
            if v == 1:
                return s
            if v % 2 == 0:
                if v // 2 not in seen:
                    dq.append((v // 2, s + 1))
                    seen.add(v // 2)
            else:
                if v + 1 not in seen:
                    dq.append((v + 1, s + 1))
                    seen.add(v + 1)
                if v - 1 not in seen:
                    dq.append((v - 1, s + 1))
                    seen.add(v - 1)
