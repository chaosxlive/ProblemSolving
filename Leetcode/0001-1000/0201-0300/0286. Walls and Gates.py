# https://leetcode.com/problems/walls-and-gates/

from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        INF = 2147483647
        dq = deque((r, c, 1) for r, R in enumerate(rooms) for c, C in enumerate(R) if C == 0)
        while len(dq):
            r, c, s = dq.popleft()
            for dr, dc in dirs:
                if 0 <= r + dr < len(rooms) and 0 <= c + dc < len(rooms[0]) and rooms[r + dr][c + dc] == INF:
                    rooms[r + dr][c + dc] = s
                    dq.append((r + dr, c + dc, s + 1))
