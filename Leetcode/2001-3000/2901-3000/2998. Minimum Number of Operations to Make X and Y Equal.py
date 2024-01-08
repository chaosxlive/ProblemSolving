# https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

from collections import deque


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        dq = deque([(y, 0)])
        seen = set([y])
        while True:
            n, s = dq.popleft()
            if n == x:
                return s
            if n < x:
                # 1
                if n * 11 not in seen:
                    dq.append((n * 11, s + 1))
                    seen.add(n * 11)
                # 2
                if n * 5 not in seen:
                    dq.append((n * 5, s + 1))
                    seen.add(n * 5)
            # 3
            if n + 1 not in seen:
                dq.append((n + 1, s + 1))
                seen.add(n + 1)
            # 4
            if n - 1 not in seen:
                dq.append((n - 1, s + 1))
                seen.add(n - 1)
