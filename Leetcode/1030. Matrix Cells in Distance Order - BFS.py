# https://leetcode.com/problems/matrix-cells-in-distance-order/

from typing import List
from collections import deque


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        walked = set([(rCenter, cCenter)])
        result = []
        q = deque([(rCenter, cCenter)])
        while q:
            r, c = q.popleft()
            result.append([r, c])
            for dr, dc in dirs:
                if 0 <= r + dr < rows and 0 <= c + dc < cols and (r + dr, c + dc) not in walked:
                    walked.add((r + dr, c + dc))
                    q.append((r + dr, c + dc))
        return result
