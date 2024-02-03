# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

from collections import deque
from typing import List


class Solution:

    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        result = [0] * n
        seen = set()
        for start in range(1, n + 1):
            seen.clear()
            seen.add(start)
            dq = deque([(start, 0)])
            while len(dq):
                h, s = dq.popleft()
                if h != start:
                    result[s - 1] += 1
                if h - 1 > 0 and h - 1 not in seen:
                    seen.add(h - 1)
                    dq.append((h - 1, s + 1))
                if h + 1 <= n and h + 1 not in seen:
                    seen.add(h + 1)
                    dq.append((h + 1, s + 1))
                if h == x and y not in seen:
                    seen.add(y)
                    dq.append((y, s + 1))
                if h == y and x not in seen:
                    seen.add(x)
                    dq.append((x, s + 1))
        return result
