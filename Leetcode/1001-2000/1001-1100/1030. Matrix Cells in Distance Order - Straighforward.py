# https://leetcode.com/problems/matrix-cells-in-distance-order/

from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        return sorted([[r, c] for r in range(rows) for c in range(cols)], key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
