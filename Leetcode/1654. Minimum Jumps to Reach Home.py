# https://leetcode.com/problems/minimum-jumps-to-reach-home/

from typing import List
from collections import deque


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        rightMost = max(max(forbidden), x) + a + b
        walked = {n: False for n in forbidden}
        q = deque([(0, 0, False)])
        while q:
            n, step, isPrevBack = q.popleft()
            if n == x:
                return step
            if not isPrevBack and n - b > 0 and n - b not in walked:
                walked[n - b] = True
                q.append((n - b, step + 1, True))
            if n + a <= rightMost and (n + a not in walked or walked[n + a] == True):
                walked[n + a] = False
                q.append((n + a, step + 1, False))
        return -1
