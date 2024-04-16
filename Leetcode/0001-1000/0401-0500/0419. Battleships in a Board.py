# https://leetcode.com/problems/battleships-in-a-board/

from collections import deque
from typing import List


class Solution:

    def countBattleships(self, board: List[List[str]]) -> int:
        LR = len(board)
        LC = len(board[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        seen = set()
        res = 0
        for r, R in enumerate(board):
            for c, C in enumerate(R):
                if C == 'X' and (r, c) not in seen:
                    res += 1
                    seen.add((r, c))
                    dq = deque([(r, c)])
                    while dq:
                        cr, cc = dq.popleft()
                        for dr, dc in dirs:
                            if 0 <= cr + dr < LR and 0 <= cc + dc < LC and board[cr + dr][cc + dc] == 'X' and (cr + dr, cc + dc) not in seen:
                                seen.add((cr + dr, cc + dc))
                                dq.append((cr + dr, cc + dc))
        return res
